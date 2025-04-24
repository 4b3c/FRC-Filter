import os, json, time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
TBA_KEY = os.getenv("TBA_KEY")

# Set the base URL for The Blue Alliance API
BASE_URL = "https://www.thebluealliance.com/api/v3"
division_keys = ['2025arc', '2025cur', '2025dal', '2025gal', '2025hop', '2025joh', '2025mil', '2025new']

# Headers to pass the API key
headers = {
    "X-TBA-Auth-Key": TBA_KEY
}

all_teams = []
for division_key in division_keys:
    # Endpoint to get the list of teams
    endpoint = f"/event/{division_key}/teams"

    # Make a GET request to the API
    response = requests.get(BASE_URL + endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200 and response.json() != []:
        print(f"Successfully retrieved data for event {division_key}: {response.status_code}")
        data = response.json()
        for team in data:
            team["division"] = division_key
        all_teams += data
    else:
        print(f"Failed to retrieve data for event {division_key}: {response.status_code}")
        break
    time.sleep(0.5)

with open("teams_from_champs.json", "w") as f:
    json.dump(all_teams, f, indent=4)
