import time
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Response
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.cache import TASKS_KEY, cache_delete, cache_get, cache_set
from app.db import Base, SessionLocal, engine
from app.models import Task


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Wait for the database to accept connections, then create tables.
    for _ in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            break
        except OperationalError:
            time.sleep(2)
    else:
        raise RuntimeError("Database not reachable")
    yield


app = FastAPI(title="DevTrack API", lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TaskCreate(BaseModel):
    title: str
    done: bool = False


def to_dict(task: Task) -> dict:
    return {"id": task.id, "title": task.title, "done": task.done}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "ok"}


@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    task = Task(title=payload.title, done=payload.done)
    db.add(task)
    db.commit()
    db.refresh(task)
    cache_delete(TASKS_KEY)  # the cached list is now stale
    return to_dict(task)


@app.get("/tasks")
def list_tasks(response: Response, db: Session = Depends(get_db)):
    cached, redis_ok = cache_get(TASKS_KEY)
    if cached is not None:
        response.headers["X-Cache"] = "HIT"
        return cached

    tasks = [to_dict(t) for t in db.query(Task).order_by(Task.id).all()]
    if redis_ok:
        cache_set(TASKS_KEY, tasks)
        response.headers["X-Cache"] = "MISS"
    else:
        response.headers["X-Cache"] = "BYPASS"
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return to_dict(task)
