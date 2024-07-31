from os import environ

from dotenv import load_dotenv

from sqlalchemy import create_engine, Engine


load_dotenv()


driver = environ["DRIVER"]
user = environ["USER"]
passwd = environ["PASSWD"]
host = environ["HOST"]
port = environ["PORT"]
name = environ["NAME"]


DATABASE_URL: str = f"{driver}://{user}:{passwd}@{host}:{port}/{name}"


def engine() -> Engine:
    return create_engine(DATABASE_URL)
