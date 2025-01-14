from fastapi import APIRouter
from app.services.mlb_data import get_player_stats, get_team_stats

router = APIRouter()

@router.get("/player_stats/{player_name}")
def fetch_player_stats(player_name: str, season: int = 2022):
    stats = get_player_stats(player_name, season)
    return {"player_stats": stats}

@router.get("/team_stats/{team_name}")
def fetch_team_stats(team_name: str, season: int = 2022):
    stats = get_team_stats(team_name, season)
    return {"team_stats": stats}
