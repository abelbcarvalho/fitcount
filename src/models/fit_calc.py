from pydantic import BaseModel

from decimal import Decimal

from src.utilities.enum.enums import (
    Gender,
    ActivityLevel,
)


class FitCalc(BaseModel):
    gender: Gender
    age: Decimal
    height: Decimal
    weight: Decimal
    level: ActivityLevel
