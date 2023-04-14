from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Operation(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: Optional[str]
    type: str
    date: datetime

    class Config:
        orm_mode = True


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: Optional[str]
    date: datetime
    type: str
