import statsapi as mlb_stats_api
from datetime import datetime, timedelta
from app.core.config import settings

async def fetch_mlb_data():
    """Fetch current MLB standings, schedule, and player stats"""
    try:
        # Get current season data
        season = datetime.now().year
        
        # Fetch essential MLB data
        data = {
            "standings": mlb_stats_api.get_standings(season),
            "schedule": mlb_stats_api.get_schedule(
                start_date=datetime.now() - timedelta(days=7),
                end_date=datetime.now() + timedelta(days=7)
            ),
            "leaders": {
                "hitting": mlb_stats_api.get_league_leaders("hitting", season),
                "pitching": mlb_stats_api.get_league_leaders("pitching", season)
            },
            "teams": mlb_stats_api.get_team_rosters(season)
        }
        
        return data
    except Exception as e:
        print(f"MLB Data Fetch Error: {str(e)}")
        return {}