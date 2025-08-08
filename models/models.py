from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from utils.db import Base

# Base would be imported when we create databse instance
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    votes = relationship('Vote', back_populates='user')

class Election(Base):
    __tablename__ = 'elections'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    candidates = relationship('Candidate', back_populates='election')
    votes = relationship('Vote', back_populates='election')

class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    election_id = Column(Integer, ForeignKey('elections.id'))
    election = relationship('Election', back_populates='candidates')
    votes = relationship('Vote', back_populates='candidate')

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    election_id = Column(Integer, ForeignKey('elections.id'))
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='votes')
    election = relationship('Election', back_populates='votes')
    candidate = relationship('Candidate', back_populates='votes')
