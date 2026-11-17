import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
name = os.environ["POSTGRES_DB"]
host = os.environ.get("POSTGRES_HOST", "pg1")

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{name}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
