import os
import google.generativeai as genai
from ..core.config import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_quiz(topic: str, difficulty: int = 3):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Generate a JSON quiz about {topic} with {5 if difficulty <3 else 10} questions.
    Difficulty level: {difficulty}/5
    Include questions about player stats, team history, and game moments.
    Format:
    {{
        "title": "Quiz Title",
        "questions": [
            {{
                "question": "Question text",
                "options": ["A", "B", "C", "D"],
                "correct": "A",
                "explanation": "Short explanation"
            }}
        ]
    }}
    """
    response = model.generate_content(prompt)
    return parse_response(response.text)

def parse_response(text: str):
    clean = text.strip().replace("```json", "").replace("```", "")
    return json.loads(clean)

if __name__ == "__main__":
    print(generate_quiz("basketball", 3))