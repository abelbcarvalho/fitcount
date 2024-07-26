from os import environ

from typing import Generator

from dotenv import load_dotenv

from sqlalchemy import create_engine, Engine


load_dotenv()


user = environ["USER"]
passwd = environ["PASSWD"]
host = environ["HOST"]
port = environ["PORT"]
name = environ["NAME"]


DATABASE_URL: str = f"postgresql://{user}:{passwd}@{host}:{port}/{name}"


async def engine() -> Generator[Engine, None, None]:
    with create_engine(DATABASE_URL) as connection:
        yield connection
