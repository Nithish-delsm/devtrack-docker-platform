from sqlalchemy import Boolean, Column, Integer, String

from app.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    done = Column(Boolean, default=False, nullable=False)
