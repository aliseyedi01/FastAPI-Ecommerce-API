from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
from typing import Final
import os
from dotenv import load_dotenv

load_dotenv()

# Establish a connection to the PostgreSQL database
# DATABASE_URL: Final = os.getenv("DATABASE_URL")
DATABASE_URL: Final = "postgresql://postgres:oO7pHDbOSQqMkr9Z@db.iytnofgxeevxxrmznquq.supabase.co:5432/postgres"
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
