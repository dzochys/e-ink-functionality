import os
from dotenv import load_dotenv
import requests
import json

# Loads the variables from .env file into the environment
load_dotenv()

# Gets the desired variable from the environment
api_key = os.getenv("GOLEMIO_API_KEY")

url = "https://api.golemio.cz/v2/pid/departureboards"

headers = {
    "accept": "application/json",
    "X-Access-Token": api_key,
}

# Filters out for desired parameters.
parameters = {
    "names": "Větrník",
    "limit": 10,
}

# Gets the data from the url with the given headers and parameters.
response = requests.get(url, headers=headers, params=parameters, timeout=15)
response.raise_for_status()

# Converts the data to python friendly formatting
data = response.json()

# Prints the data in an easily readable format.
print(json.dumps(data, indent=2, ensure_ascii=False)) # ensure_ascii=False preserves the czech characters in normal format
