import MLBStatsAPI as mlb

api = mlb.MLBStatsAPI()

def get_player_stats(player_name: str, season: int = 2022):
    player_id = api.get_people_id(player_name)[0]
    stats = ["season", "seasonAdvanced"]
    groups = ["hitting"]
    params = {"season": season}
    player_stats = api.get_player_stats(player_id, stats, groups, **params)
    return player_stats

def get_team_stats(team_name: str, season: int = 2022):
    team_id = api.get_team_id(team_name)[0]
    team_stats = api.get_team_stats(team_id, stats, groups, **params)
    return team_stats
