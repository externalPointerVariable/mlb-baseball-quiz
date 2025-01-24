from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base  # Single import for Base

class Achievement(Base):
    __tablename__ = "achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    description = Column(String(255))
    icon = Column(String(255))  # URL to achievement icon
    criteria_type = Column(String(50))  # 'xp', 'quiz_count', 'perfect_score', etc
    threshold = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_achievements = relationship("UserAchievement", back_populates="achievement")

class UserAchievement(Base):
    __tablename__ = "user_achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    achievement_id = Column(Integer, ForeignKey("achievements.id"))
    unlocked_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships with back_populates
    user = relationship("User", back_populates="achievements")
    achievement = relationship("Achievement", back_populates="user_achievements")