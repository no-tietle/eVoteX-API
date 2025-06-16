from fastapi import FastAPI
from .database.db import engine, get_db
from . import models,schema,routing

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}