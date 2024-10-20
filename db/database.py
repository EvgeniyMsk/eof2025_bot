from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from bot_config import main_config

SQLALCHEMY_DATABASE_URL = main_config.connection_string

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10
)

session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


# def get_db():
#     db = async_session()
#     try:
#         yield db
#     finally:
#         db.close()
