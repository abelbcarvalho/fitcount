from decimal import Decimal

from pydantic import BaseModel


class Weight(BaseModel):
    person_id: int

    weight: Decimal
