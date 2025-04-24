import os, json, time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
TBA_KEY = os.getenv("TBA_KEY")

# Set the base URL for The Blue Alliance API
BASE_URL = "https://www.thebluealliance.com/api/v3"

# Headers to pass the API key
headers = {
    "X-TBA-Auth-Key": TBA_KEY
}


# Endpoint to get the list of teams
endpoint = f"/events/2025"

# Make a GET request to the API
response = requests.get(BASE_URL + endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200 and response.json() != []:
    print(f"Successfully retrieved data: {response.status_code}")
    with open("events.json", "w") as f:
        json.dump(response.json(), f, indent=4)
else:
    print(f"Failed to retrieve data: {response.status_code}")

