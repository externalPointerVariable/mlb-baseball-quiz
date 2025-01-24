# app/services/quiz_generation.py
from app.services import gemini, mlb_data

async def generate_quiz_with_mlb(topic: str, difficulty: int = 3):
    """Generate quiz using both Gemini and MLB stats"""
    mlb_context = mlb_data.get_relevant_context(topic)
    
    prompt = f"""
    Generate a baseball quiz using this MLB data:
    {mlb_context}
    
    Topic: {topic}
    Difficulty: {difficulty}/5
    Include questions about:
    - Recent player performance
    - Team standings
    - Historical comparisons
    - Game strategies
    
    Format questions with 4 options and mark correct answers.
    """
    
    return await gemini.generate_quiz(prompt)