from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from bot_config import main_config

SQLALCHEMY_DATABASE_URL = main_config.connection_string

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
