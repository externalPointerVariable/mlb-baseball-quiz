# app/routers/preferences.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session_local, User
from app.users import current_user

router = APIRouter()

async def get_db():
    async with async_session_local() as session:
        yield session

@router.get("/preferences")
async def read_preferences(user: User = Depends(current_user), db: AsyncSession = Depends(get_db)):
    return {"user_id": user.id, "preferences": "User preferences here"}
