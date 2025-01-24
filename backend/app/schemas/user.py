from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: str | None = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    favorite_team: str | None
    favorite_player: str | None

class User(UserBase):
    id: int
    xp: int
    level: int
    
    class Config:
        orm_mode = True