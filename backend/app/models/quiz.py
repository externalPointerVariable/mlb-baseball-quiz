from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id: Mapped[int] = mapped_column(Column(Integer, primary_key=True, index=True))
    title: Mapped[str] = mapped_column(Column(String))
    topic: Mapped[str] = mapped_column(Column(String))
    created_by: Mapped[int] = mapped_column(Column(Integer, ForeignKey("users.id")))


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Column(Integer, primary_key=True))
    quiz_id: Mapped[int] = mapped_column(Column(Integer, ForeignKey("quizzes.id")))
    question_text: Mapped[str] = mapped_column(Column(String))
    options: Mapped[dict] = mapped_column(Column(JSON))
    correct_answer: Mapped[str] = mapped_column(Column(String))
    explanation: Mapped[str] = mapped_column(Column(String))
    

class UserScore(Base):
    __tablename__ = "user_scores"

    id: Mapped[int] = mapped_column(Column(Integer, primary_key=True))
    user_id: Mapped[int] = mapped_column(Column(Integer, ForeignKey("users.id")))
    quiz_id: Mapped[int] = mapped_column(Column(Integer, ForeignKey("quizzes.id")))
    score: Mapped[int] = mapped_column(Column(Integer))
