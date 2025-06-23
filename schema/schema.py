from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True

# Election Schemas
class ElectionBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

class ElectionCreate(ElectionBase):
    pass

class ElectionRead(ElectionBase):
    id: int
    candidates: Optional[List['CandidateRead']] = None

    class Config:
        orm_mode = True

# Candidate Schemas
class CandidateBase(BaseModel):
    name: str
    election_id: int

class CandidateCreate(CandidateBase):
    pass

class CandidateRead(CandidateBase):
    id: int
    votes: Optional[List['VoteRead']] = None

    class Config:
        orm_mode = True

# Vote Schemas
class VoteBase(BaseModel):
    user_id: int
    election_id: int
    candidate_id: int

class VoteCreate(VoteBase):
    pass

class VoteRead(VoteBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# For forward references
ElectionRead.update_forward_refs()
CandidateRead.update_forward_refs()


