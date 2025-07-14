from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID
from enum import Enum

class ElectionsBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    created_by: UUID
    is_active: bool
    created_at: datetime


class RoleEnum(Enum):
    VOTER = "voter"
    ADMIN = "admin"
    AUDITOR = "auditor"


class UsersBase(BaseModel):
    email: EmailStr
    full_name: str
    role: RoleEnum
    is_verified: bool
    created_at: datetime


class CandidatesBase(BaseModel):
    election_id: UUID
    name: str
    description: str
    image_url: str
    created_at: datetime


class VotesBase(BaseModel):
    election_id: UUID
    candidate_id: UUID
    encrypted_votes: str
    receipt_hash: str
    created_at: datetime


class Voter_Elections(BaseModel):
    user_id: UUID
    elections_id: UUID
    has_voted: bool
    
