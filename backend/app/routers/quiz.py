from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.gemini import generate_quiz
from sqlalchemy.future import select
from app.db import get_db
from app.models.quiz import Quiz, Question
from app.schemas.quiz import QuizCreate, QuizResponse

router = APIRouter()  # <-- Router initialization is correct

@router.post("/generate", response_model=QuizResponse)
async def generate_new_quiz(
    topic: str,
    db: AsyncSession = Depends(get_db)  # Use AsyncSession for async DB operations
):
    try:
        quiz_data = generate_quiz(topic)

        db_quiz = Quiz(title=quiz_data["title"], topic=topic)
        db.add(db_quiz)
        await db.flush()  # Ensure the quiz gets added before we add the questions

        # Create questions and add to the session
        questions = [
            Question(
                quiz_id=db_quiz.id,
                question_text=q["question_text"],
                options=q["options"],
                correct_answer=q["correct_answer"]
            )
            for q in quiz_data["questions"]
        ]
        
        db.add_all(questions)  # Add all questions in one go to optimize
        await db.commit()  # Commit once after both quiz and questions are added

        return db_quiz  # Returning the quiz, it will be converted to QuizResponse automatically

    except Exception as e:
        await db.rollback()  # Ensure async rollback in case of error
        raise HTTPException(status_code=500, detail=f"Quiz generation failed: {str(e)}")

@router.post("/{quiz_id}/submit")
async def submit_quiz(
    quiz_id: int,
    answers: dict,
    db: AsyncSession = Depends(get_db)  # Use AsyncSession
):
    try:
        # Fetch questions for the given quiz
        questions = await db.execute(
            select(Question).filter(Question.quiz_id == quiz_id)
        )
        questions = questions.scalars().all()

        # Calculate score by comparing the answers
        score = sum(1 for q in questions if str(q.id) in answers and answers[str(q.id)] == q.correct_answer)
        
        return {"score": score}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error submitting quiz: {str(e)}")
