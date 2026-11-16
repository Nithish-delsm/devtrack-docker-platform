from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="DevTrack API")

# Temporary in-memory storage. Lost on every restart (PostgreSQL fixes this later).
tasks: List[dict] = []


class TaskCreate(BaseModel):
    title: str
    done: bool = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = {"id": len(tasks) + 1, **task.dict()}
    tasks.append(new_task)
    return new_task


@app.get("/tasks")
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
