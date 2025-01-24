from pydantic import BaseModel
from typing import List

class QuestionBase(BaseModel):
    question_text: str
    options: List[str]
    correct_answer: str

class QuizCreate(BaseModel):
    title: str
    topic: str
    questions: List[QuestionBase]

class QuizResponse(QuizCreate):
    id: int

    class Config:
        orm_mode = True