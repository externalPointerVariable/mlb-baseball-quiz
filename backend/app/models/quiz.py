from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from .base import Base

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    topic = Column(String)
    created_by = Column(Integer, ForeignKey("users.id"))

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    question_text = Column(String)
    options = Column(JSON)
    correct_answer = Column(String)
    explanation = Column(String)

class UserScore(Base):
    __tablename__ = "user_scores"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)