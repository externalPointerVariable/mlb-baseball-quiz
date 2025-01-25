from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, async_session, Base
from app.routers import auth, quiz, profile
from app.services.mlb_data import fetch_mlb_data
from app.core.config import settings

app = FastAPI(title="MLB Quiz API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(quiz.router, prefix="/api/quizzes")
app.include_router(profile.router, prefix="/api/profile")

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with async_session() as db:
        await load_achievements(db)
    
    app.state.mlb_data = await fetch_mlb_data()

@app.get("/")
async def health_check():
    return {
        "status": "running",
        "database": settings.DATABASE_URL,
        "mlb_data": bool(app.state.mlb_data)
    }