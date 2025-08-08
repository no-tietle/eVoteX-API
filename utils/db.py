from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL='sqlite:///.sql.db'
engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker(bind=engine,autocommit=false,autoflush=false)