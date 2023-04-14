from pydantic import BaseModel
from datetime import datetime


class Tracked(BaseModel):
    id: int
    first_currency: str
    second_currency: str
    date_at: datetime

    class Config:
        orm_mode = True
