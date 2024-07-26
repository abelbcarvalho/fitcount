from datetime import datetime

from decimal import Decimal

from sqlalchemy import (
    String,
    DateTime,
    Numeric,
    Integer,
    ForeignKey,
)

from sqlalchemy.orm import (
    mapped_column,
    relationship,
    Mapped,
)

from src.db.models.base import Base


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
