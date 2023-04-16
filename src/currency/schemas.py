from http.client import HTTPException

from pydantic import BaseModel
from datetime import datetime

from pydantic.class_validators import validator


class Tracked(BaseModel):
    id: int
    first_currency: str
    second_currency: str
    date_at: datetime

    class Config:
        orm_mode = True


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

