from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic.class_validators import validator, root_validator


class CurrencyName(str, Enum):
    USD = "USD"
    RUB = "RUB"
    KZT = "KZT"
    ARS = "ARS"
    TRY = "TRY"
    EUR = "EUR"


class Tracked(BaseModel):
    first_currency: CurrencyName
    second_currency: CurrencyName
    # date_at: Optional[datetime]

    class Config:
        orm_mode = True

    @root_validator
    def validate_op1(cls, value):
        if not value.get('first_currency') != value.get('second_currency'):
            raise HTTPException(status_code=400, detail="Currencies do not have to match")
        return value


# class OperationAddTrack(BaseModel):
#     first_currency: str
#     second_currency: str
#
#     @validator("first_currency")
#     def validate_op1(cls, value):
#         if not len(value) == 3:
#             raise HTTPException(
#                 status_code=405, detail='adsadad'
#             )
#         return value

