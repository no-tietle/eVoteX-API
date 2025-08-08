from ..utils.db import Sessionlocal
from sqlalchemy.orm import Session
from ..models.models import *
from ..schema.schema import *
from fastapi import HTTPException,status

def get_db():
    db = Sessionlocal()
    try:
        yield db
    
    except Exception as e:
        print(f"An error occured with db connection {e}")
    finally:
        db.close()
    

def create_election(db:Session, elecion:ElectionCreate):
    db_election = Election(**election.dict())
    db.add(db_election)
    db.commit()
    db.refresh(db_election)

    return db_election


def get_election_by_id(db:Session, id:int):
    return db.query(Election).filter(Election.id == id).first()


def get_all_elections(db:Session,skip:int = 0, limit:int = 100):
    
    return db.query(Election).offset(skip).limit(limit).all()



def delete_election_id(db:Session,id:int):

    # 1st method by performing query and deletion on same line
    db.query(Election).delete(Election.id == id)
    return None

    # second: retrieve election if its available and delete else return an error
    db_election = db.query(Election).filter(Election.id == id).first()

    if not db_election:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Election by id not found")
    
    else:
        db.delete(db_election)
        db.commit()
    
    return

