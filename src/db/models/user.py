from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
)

from sqlalchemy.orm import (
    mapped_column,
    Mapped
)

from src.db.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    passwd: Mapped[str] = mapped_column(String(255))

    createAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updateAt: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now())
