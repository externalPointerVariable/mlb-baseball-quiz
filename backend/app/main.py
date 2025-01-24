from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routers import auth, quiz, profile
from app.services.mlb_data import fetch_mlb_data
from app.core.config import settings

# Create tables (only for development)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Initialize FastAPI app
app = FastAPI(title="MLB Quiz API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(quiz.router, prefix="/api/quizzes")
app.include_router(profile.router, prefix="/api/profile")

# MLB Data Integration
@app.on_event("startup")
async def startup_event():
    await create_tables()
    # Pre-fetch MLB data on startup
    app.state.mlb_data = await fetch_mlb_data()
    print("✅ MLB data loaded successfully")

# Health check endpoint
@app.get("/")
async def root():
    return {
        "message": "MLB Quiz API Running",
        "mlb_data_version": app.state.mlb_data.get('meta', {}).get('version')
    }