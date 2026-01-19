import requests
import json
import os

# Secrets are pulled from GitHub Actions environment
CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('STRAVA_REFRESH_TOKEN')
ATHLETE_ID = '294060'

def fetch_data():
    # 1. Refresh the token to get access
    auth_res = requests.post('https://www.strava.com/oauth/token', data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN,
        'grant_type': 'refresh_token'
    })
    access_token = auth_res.json().get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}

    # 2. Get last 5 activities
    activities = requests.get('https://www.strava.com/api/v3/athlete/activities?per_page=5', headers=headers).json()

    # 3. Get YTD totals
    stats = requests.get(f'https://www.strava.com/api/v3/athletes/{ATHLETE_ID}/stats', headers=headers).json()

    # 4. Save to Hugo data folder
    os.makedirs('data', exist_ok=True)
    with open('data/strava.json', 'w') as f:
        json.dump(activities, f)
    with open('data/strava_stats.json', 'w') as f:
        json.dump(stats, f)

if __name__ == "__main__":
    fetch_data()
