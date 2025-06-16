from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserBaseModel(BaseModel):
    id:UUID
    first_name : str
    last_name : str
    email: str


class VotingBaseModle(BaseModel):
    id: UUID
    title:str
    description:str
    start_date : datetime
    closing_date : datetime


