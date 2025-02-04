import requests
import json
from django.http import JsonResponse

def process_endpoint_url(endpoint_url):
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}


def baseball_leagues(request):
    try:
        sports_endpoint_url = 'https://statsapi.mlb.com/api/v1/sports'
        sports_data = process_endpoint_url(sports_endpoint_url)
        return JsonResponse(sports_data['sports'], safe=False, json_dumps_params={'indent': 4})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def baseball_teams(request):
    try:
        sports_id = request.body.decode('utf-8')
        sports_id = json.loads(sports_id)
        sports_id = sports_id['sports_id']
        teams_endpoint_url = f'https://statsapi.mlb.com/api/v1/teams?sportId={sports_id}'
        teams_data = process_endpoint_url(teams_endpoint_url)
        return JsonResponse(teams_data['teams'], safe=False, json_dumps_params={'indent': 4})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def baseball_players(request):
    try:
        team_id = request.body.decode('utf-8')
        team_id = json.loads(team_id)
        team_id = team_id['team_id']
        players_endpoint_url = f'https://statsapi.mlb.com/api/v1/teams/{team_id}/roster'
        players_data = process_endpoint_url(players_endpoint_url)
        return JsonResponse(players_data['roster'], safe=False, json_dumps_params={'indent': 4})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

# print(baseball_teams(1))