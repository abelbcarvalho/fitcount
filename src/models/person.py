from decimal import Decimal

from typing import Optional

from pydantic import BaseModel

from src.utilities.enum.enums import Gender


class Person(BaseModel):
    user_id: int

    first_name: str
    last_name: str
    gender: Gender
    weight: Decimal
    height: Optional[Decimal] = None
