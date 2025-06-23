from fastapi import FastAPI
from .database.db import engine, get_db
from . import models, schema
from routing.routing import router

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}