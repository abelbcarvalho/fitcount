from typing import List

from pydantic import BaseModel

from src.utilities.enum.enums import TrainingType


class Training(BaseModel):
    person_id: int

    type_training: TrainingType
    trainings: List[str]
    descript: str
