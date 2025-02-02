import requests
import json
from django.http import JsonResponse

def process_endpoint_url(endpoint_url):
    try:
        json_result = requests.get(endpoint_url).content
        data = json.loads(json_result)
        return data
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def baseball_leagues(request):
    try:
        sports_endpoint_url = 'https://statsapi.mlb.com/api/v1/sports'
        sports_data = process_endpoint_url(sports_endpoint_url)
        return JsonResponse(sports_data['sports'], safe=False, json_dumps_params={'indent': 4})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def baseball_teams(sports_id):
    try:
        teams_endpoint_url = f'https://statsapi.mlb.com/api/v1/teams?sportId={sports_id}'
        teams_data = process_endpoint_url(teams_endpoint_url)
        return json.dumps(teams_data['teams'], indent=4)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def baseball_players(request, team_id):
    try:
        players_endpoint_url = f'https://statsapi.mlb.com/api/v1/teams/{team_id}/roster'
        players_data = process_endpoint_url(players_endpoint_url)
        return json.dumps(players_data['roster'], indent=4)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# print(baseball_teams(1))