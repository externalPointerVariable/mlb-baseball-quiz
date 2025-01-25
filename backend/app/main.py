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
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(quiz.router, prefix="/api/quizzes")
app.include_router(profile.router, prefix="/api/profile")

@app.on_event("startup")
async def startup_event():
    try:
        # Create database tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
        # Initialize data
        async with async_session() as session:
            await load_achievements(session)  # Ensure this is async
        
        # Fetch MLB data async
        app.state.mlb_data = await fetch_mlb_data()
    except Exception as e:
        print(f"Startup error: {e}")
        app.state.mlb_data = None

@app.get("/")
async def health_check():
    return {
        "status": "running",
        "database": settings.DATABASE_URL,
        "mlb_data_loaded": bool(app.state.mlb_data),
        "mlb_data_count": len(app.state.mlb_data) if app.state.mlb_data else 0,
    }
