from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name: str | None = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    favorite_team: str | None = None
    favorite_player: str | None = None

class UserResponse(UserBase):
    id: int
    favorite_team: str | None
    favorite_player: str | None
    xp: int
    level: int

    class Config:
        orm_mode = True