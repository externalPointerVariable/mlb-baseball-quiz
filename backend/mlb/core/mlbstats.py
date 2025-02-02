import requests
import json
from django.http import JsonResponse

def process_endpoint_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTP errors
    return response.json()  # Return parsed JSON data (dict)


def baseball_leagues(request):
    try:
        sports_endpoint_url = 'https://statsapi.mlb.com/api/v1/sports'
        sports_data = process_endpoint_url(sports_endpoint_url)
        return JsonResponse(sports_data['sports'], safe=False, json_dumps_params={'indent': 4})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

# mlbstats.py
def baseball_teams(sports_id):  # ✅ Accepts integer, not request
    try:
        url = f'https://statsapi.mlb.com/api/v1/teams?sportId={sports_id}'
        teams_data = process_endpoint_url(url)
        return teams_data  # Return raw data (dict/list)
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}  # Return dict for errors
    

def baseball_players(request, team_id):
    try:
        players_endpoint_url = f'https://statsapi.mlb.com/api/v1/teams/{team_id}/roster'
        players_data = process_endpoint_url(players_endpoint_url)
        return json.dumps(players_data['roster'], indent=4)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

print(baseball_teams(1))