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

full_data = []
page = 0
while True:
    # Endpoint to get the list of teams
    endpoint = f"/teams/{page}"

    # Make a GET request to the API
    response = requests.get(BASE_URL + endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200 and response.json() != []:
        print(f"Successfully retrieved data for page {page}: {response.status_code}")
        full_data.append(response.json())
    else:
        print(f"Failed to retrieve data for page {page}: {response.status_code}")
        break
    time.sleep(0.5)
    page += 1

with open("data.json", "w") as f:
    json.dump(full_data, f, indent=4) 
