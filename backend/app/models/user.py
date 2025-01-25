from sqlalchemy import Column, Integer, String
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Column(Integer, primary_key=True, index=True))
    email: Mapped[str] = mapped_column(Column(String, unique=True, index=True))
    name: Mapped[str] = mapped_column(Column(String))
    hashed_password: Mapped[str] = mapped_column(Column(String))
    favorite_team: Mapped[str] = mapped_column(Column(String))
    favourite_player: Mapped[str] = mapped_column(Column(String))
    xp: Mapped[int] = mapped_column(Column(Integer, default=0))
    level: Mapped[int] = mapped_column(Column(Integer, default=1))
    