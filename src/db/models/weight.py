from datetime import datetime

from decimal import Decimal

from sqlalchemy import (
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


class Weight(Base):
    __tablename__ = "weigths"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("persons.id"))
    weight: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    person = relationship("Person", back_populates="weights")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)
