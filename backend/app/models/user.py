from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    google_id = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    picture = Column(String)
    favorite_team = Column(String)
    favorite_player = Column(String)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    achievements = Column(JSON, default=[])
    achievements = relationship("UserAchievement", back_populates="user")
    total_quizzes = Column(Integer, default=0)
    perfect_scores = Column(Integer, default=0)
    consecutive_days = Column(Integer, default=0)