from fastapi import APIRouter
from app.services.content_generation import generate_text

router = APIRouter()

@router.post("/generate_text/")
def generate_personalized_text(data: dict):
    prompt = data.get("prompt", "")
    content = generate_text(prompt)
    return {"content": content}
