from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud
from schema import schema

router = APIRouter()

# Dependency
def get_db():
    db = crud.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User Routes
@router.post('/users/', response_model=schema.UserRead)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get('/users/{user_id}', response_model=schema.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user

@router.get('/users/', response_model=list[schema.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

# Election Routes
@router.post('/elections/', response_model=schema.ElectionRead)
def create_election(election: schema.ElectionCreate, db: Session = Depends(get_db)):
    return crud.create_election(db, election)

@router.get('/elections/{election_id}', response_model=schema.ElectionRead)
def read_election(election_id: int, db: Session = Depends(get_db)):
    db_election = crud.get_election(db, election_id)
    if db_election is None:
        raise HTTPException(status_code=404, detail='Election not found')
    return db_election

@router.get('/elections/', response_model=list[schema.ElectionRead])
def read_elections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_elections(db, skip=skip, limit=limit)

# Candidate Routes
@router.post('/candidates/', response_model=schema.CandidateRead)
def create_candidate(candidate: schema.CandidateCreate, db: Session = Depends(get_db)):
    return crud.create_candidate(db, candidate)

@router.get('/candidates/{candidate_id}', response_model=schema.CandidateRead)
def read_candidate(candidate_id: int, db: Session = Depends(get_db)):
    db_candidate = crud.get_candidate(db, candidate_id)
    if db_candidate is None:
        raise HTTPException(status_code=404, detail='Candidate not found')
    return db_candidate

@router.get('/candidates/', response_model=list[schema.CandidateRead])
def read_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_candidates(db, skip=skip, limit=limit)

# Vote Routes
@router.post('/votes/', response_model=schema.VoteRead)
def create_vote(vote: schema.VoteCreate, db: Session = Depends(get_db)):
    return crud.create_vote(db, vote)

@router.get('/votes/{vote_id}', response_model=schema.VoteRead)
def read_vote(vote_id: int, db: Session = Depends(get_db)):
    db_vote = crud.get_vote(db, vote_id)
    if db_vote is None:
        raise HTTPException(status_code=404, detail='Vote not found')
    return db_vote

@router.get('/votes/', response_model=list[schema.VoteRead])
def read_votes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_votes(db, skip=skip, limit=limit)
