from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    name: str
    email: str
    password: str
    async def create_user(user: user):
        return user

@app.get("/")
async def root():
    return {"message": "Welcome ti mlb-personalized-ai-api"}

@app.post("/user")
async def create_user(user: user):
    return user.create_user(user)