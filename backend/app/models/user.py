from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    favorite_team = Column(String)
    favorite_player = Column(String)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)