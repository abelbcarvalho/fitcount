from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    passwd: str
    email: Optional[str] = None
