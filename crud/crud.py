from ..database.db import SessionLocal
from sqlalchemy.orm import Session
from models.models import User, Election, Candidate, Vote
from schema.schema import UserCreate, ElectionCreate, CandidateCreate, VoteCreate

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User CRUD

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Election CRUD

def create_election(db: Session, election: ElectionCreate):
    db_election = Election(**election.dict())
    db.add(db_election)
    db.commit()
    db.refresh(db_election)
    return db_election

def get_election(db: Session, election_id: int):
    return db.query(Election).filter(Election.id == election_id).first()

def get_elections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Election).offset(skip).limit(limit).all()

# Candidate CRUD

def create_candidate(db: Session, candidate: CandidateCreate):
    db_candidate = Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def get_candidate(db: Session, candidate_id: int):
    return db.query(Candidate).filter(Candidate.id == candidate_id).first()

def get_candidates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Candidate).offset(skip).limit(limit).all()

# Vote CRUD

def create_vote(db: Session, vote: VoteCreate):
    db_vote = Vote(**vote.dict())
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

def get_vote(db: Session, vote_id: int):
    return db.query(Vote).filter(Vote.id == vote_id).first()

def get_votes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vote).offset(skip).limit(limit).all()

