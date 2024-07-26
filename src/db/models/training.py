from datetime import datetime

from typing import List

from src.utilities.enum.enums import TrainingType

from sqlalchemy import (
    String,
    DateTime,
    Integer,
    ForeignKey,
    Enum,
    ARRAY,
)

from sqlalchemy.orm import (
    mapped_column,
    relationship,
    Mapped,
)

from src.db.models.base import Base


class Training(Base):
    __tablename__ = "trainings"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("persons.id"))
    type_training: Mapped[TrainingType] = mapped_column(Enum(TrainingType))
    trainings: Mapped[List[str]] = mapped_column(ARRAY(String))
    descript: Mapped[str] = mapped_column(String(128), nullable=True)

    person = relationship("Person", back_populates="trainings")
    kilo_calories = relationship("KiloCalorie", back_populates="training")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)
