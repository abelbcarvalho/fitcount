from decimal import Decimal

from typing import Optional

from pydantic import BaseModel


class Person(BaseModel):
    user_id: int

    first_name: str
    last_name: str
    weight: Decimal
    height: Optional[Decimal] = None
