from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime

class UserBaseModel(BaseModel):
    id:UUID
    first_name : str
    last_name : str
    email: EmailStr


class VotingBaseModle(BaseModel):
    id: UUID
    title:str
    description:str
    start_date : datetime
    closing_date : datetime


