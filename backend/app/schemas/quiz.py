from pydantic import BaseModel, Field
from typing import List, Optional

class QuestionBase(BaseModel):
    question_text: str = Field(..., max_length=500, description="The question text")
    options: List[str] = Field(..., min_items=2, max_items=4, description="List of options for the question")
    correct_answer: str = Field(..., description="The correct answer option")

    @root_validator
    async def validate_correct_answer(cls, values):
        if values["correct_answer"] not in values["options"]:
            raise ValueError("The correct answer must be one of the options")
        return values

class QuizCreate(BaseModel):
    title: str = Field(..., max_length=255, description="The title of the quiz")
    topic: str = Field(..., max_length=255, description="The topic of the quiz")
    questions: List[QuestionBase] = Field(..., min_items=1, description="List of questions for the quiz")

class QuizResponse(QuizCreate):
    id: int = Field(..., description="Unique identifier of the quiz")

    class Config:
        orm_mode = True  # Enables conversion from SQLAlchemy models to Pydantic models
