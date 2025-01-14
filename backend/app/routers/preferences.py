from fastapi import APIRouter, HTTPException
from app.models.user import UserPreferences

router = APIRouter()

# In-memory storage for simplicity
user_preferences_db = {}

@router.post("/set_preferences/")
def set_preferences(preferences: UserPreferences):
    user_preferences_db[preferences.user_id] = preferences
    return {"message": "Preferences saved successfully"}

@router.get("/get_preferences/{user_id}")
def get_preferences(user_id: str):
    preferences = user_preferences_db.get(user_id)
    if preferences is None:
        raise HTTPException(status_code=404, detail="User not found")
    return preferences
