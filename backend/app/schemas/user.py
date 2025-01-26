from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
import re

class UserBase(BaseModel):
    email: EmailStr
    name: str | None = None

class UserCreate(UserBase):
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=128, 
        description="Password must be between 8 and 128 characters"
    )

    @validator("password")
    def validate_password(cls, value):
        if not re.search(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])", value):
            raise ValueError(
                "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"
            )
        return value

class UserUpdate(BaseModel):
    favorite_team: str | None = None
    favorite_player: str | None = None

class UserResponse(UserBase):
    id: int
    favorite_team: str | None = None
    favorite_player: str | None = None
    xp: int = 0
    level: int = 1

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "email": "user@example.com",
                "name": "John Doe",
                "favorite_team": "Yankees",
                "favorite_player": "Derek Jeter",
                "xp": 1500,
                "level": 5,
            }
        }
