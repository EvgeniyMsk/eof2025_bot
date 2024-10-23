from dotenv import load_dotenv
import os
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

load_dotenv('dev.env')

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
FILE_LOCATION = os.getenv("FILE_LOCATION")


class MainConfigModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class MainConfig(MainConfigModel):
    bot_token: str = Field()
    database_url: str = Field()
    database_name: str = Field()
    database_username: str = Field()
    database_password: str = Field()
    database_port: str = Field()
    file_location: str = Field()
    connection_string: str = Field()


main_config = MainConfig(
    bot_token=BOT_TOKEN,
    database_url=DB_HOST,
    database_name=DB_NAME,
    database_username=DB_USER,
    database_password=DB_PASS,
    database_port=DB_PORT,
    file_location=FILE_LOCATION,
    connection_string=f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)