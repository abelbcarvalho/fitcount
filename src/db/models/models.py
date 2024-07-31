from datetime import datetime
from decimal import Decimal
from typing import List

from sqlalchemy import String, Integer, ForeignKey, Enum, Numeric, DateTime, ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

from src.utilities.enum.enums import Gender, TrainingType

from src.db.connection import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_name: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    passwd: Mapped[str] = mapped_column(String(255))

    persons = relationship("Person", back_populates="user")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(128))
    gender: Mapped[Gender] = mapped_column(Enum(Gender))
    height: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    weight: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    user = relationship("User", back_populates="persons")
    weights = relationship("Weight", back_populates="person")
    trainings = relationship("Training", back_populates="person")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)


class Training(Base):
    __tablename__ = "trainings"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("persons.id"))
    type_training: Mapped[TrainingType] = mapped_column(Enum(TrainingType))
    trainings: Mapped[List[str]] = mapped_column(ARRAY(String))
    descript: Mapped[str] = mapped_column(String(128))

    person = relationship("Person", back_populates="trainings")
    kilo_calories = relationship("KiloCalorie", back_populates="training")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)


class Weight(Base):
    __tablename__ = "weigths"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("persons.id"))

    weight: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    person = relationship("Person", back_populates="weights")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)


class KiloCalorie(Base):
    __tablename__ = "kilo_calories"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("trainings.id"))

    descript: Mapped[str] = mapped_column(String(32))
    series: Mapped[int] = mapped_column(Integer)
    times: Mapped[int] = mapped_column(Integer)
    minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    calories: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    training = relationship("Training", back_populates="kilo_calories")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)


engine = engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
