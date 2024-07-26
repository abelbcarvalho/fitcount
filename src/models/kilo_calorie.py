from decimal import Decimal

from typing import Optional

from pydantic import BaseModel


class KiloCalorie(BaseModel):
    person_id: int

    descript: str
    series: int
    times: int
    calories: Decimal
    minutes: Optional[int] = None
