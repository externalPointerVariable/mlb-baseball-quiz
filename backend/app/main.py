from fastapi import FastAPI
from app.routers import preferences, content, mlb_data
from db import app as auth_app

app = FastAPI()

# Include the authentication app
app.mount("/auth", auth_app)

app.include_router(preferences.router, prefix="/api/preferences")
app.include_router(content.router, prefix="/api/content")
app.include_router(mlb_data.router, prefix="/api/mlb_data")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personalized Fan Highlights API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
