from fastapi import FastAPI
from schema import schema



app = FastAPI()

@app.get("/")
def home():
    return {"Data": "First Project"}

@app.post("/users")
def users_create(users: schema.UsersCreate):
    return {"Data": "Create Users"}