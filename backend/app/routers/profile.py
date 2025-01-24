from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate

router = APIRouter()  # This was missing

@router.get("/me", response_model=UserResponse)
async def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return current_user

@router.patch("/preferences", response_model=UserResponse)
async def update_preferences(
    preferences: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if preferences.favorite_team:
        current_user.favorite_team = preferences.favorite_team
    if preferences.favorite_player:
        current_user.favorite_player = preferences.favorite_player
    
    db.commit()
    db.refresh(current_user)
    return current_user