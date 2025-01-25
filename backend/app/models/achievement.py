from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

class Achievement(Base):
    __tablename__ = "achievements"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    icon: Mapped[str] = mapped_column(String(255))
    crieteria_type: Mapped[str] = mapped_column(String(255))
    threshold: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    # Async-compatible relationship
    user_achievements = relationship(
        "UserAchievement", 
        back_populates="achievement",
        lazy="raise"  # Prevent implicit sync IO
    )

class UserAchievement(Base):
    __tablename__ = "user_achievements"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    achievement_id: Mapped[int] = mapped_column(Integer, ForeignKey("achievements.id"))
    unlocked_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    # Async relationships with explicit loading strategy
    user = relationship(
        "User", 
        back_populates="achievements",
        lazy="raise"  # Force explicit loading
    )
    
    achievement = relationship(
        "Achievement", 
        back_populates="user_achievements",
        lazy="raise"  # Prevent implicit sync queries
    )
