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


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(128))
    height: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    weight: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    user = relationship("User", back_populates="persons")
    weights = relationship("Weight", back_populates="person")

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=True)
