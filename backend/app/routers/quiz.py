from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.gemini import generate_quiz
from app.db import get_db
from app.models.quiz import Quiz, Question
from app.schemas.quiz import QuizCreate, QuizResponse

router = APIRouter()  # <-- This was missing

@router.post("/generate", response_model=QuizResponse)
async def generate_new_quiz(
    topic: str,
    db: Session = Depends(get_db)
):
    try:
        quiz_data = generate_quiz(topic)
        
        db_quiz = Quiz(title=quiz_data["title"], topic=topic)
        db.add(db_quiz)
        db.commit()
        
        for q in quiz_data["questions"]:
            db_question = Question(
                quiz_id=db_quiz.id,
                question_text=q["question_text"],
                options=q["options"],
                correct_answer=q["correct_answer"]
            )
            db.add(db_question)
        
        db.commit()
        return db_quiz
        
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Quiz generation failed: {str(e)}")

@router.post("/{quiz_id}/submit")
async def submit_quiz(
    quiz_id: int,
    answers: dict,
    db: Session = Depends(get_db)
):
    questions = db.query(Question).filter(Question.quiz_id == quiz_id).all()
    score = sum(1 for q in questions if str(q.id) in answers and answers[str(q.id)] == q.correct_answer)
    return {"score": score}