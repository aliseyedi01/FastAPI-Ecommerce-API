from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
from app.core.config import settings


DATABASE_URL = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

# Establish a connection to the PostgreSQL database
engine = create_engine(DATABASE_URL)


# Create database tables based on the defined SQLAlchemy models (subclasses of the Base class)
Base = declarative_base()
Base.metadata.create_all(engine)


# Connect to the database and provide a session for interacting with it
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
