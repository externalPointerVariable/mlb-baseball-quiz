from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128, description="Password must be between 8 and 128 characters")

class UserUpdate(BaseModel):
    favorite_team: Optional[str] = None
    favorite_player: Optional[str] = None

class UserResponse(UserBase):
    id: int
    favorite_team: Optional[str] = None
    favorite_player: Optional[str] = None
    xp: int
    level: int

    class Config:
        orm_mode = True  # Enables conversion from SQLAlchemy models to Pydantic models
