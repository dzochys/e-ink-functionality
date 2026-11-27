import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime

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
    "names": "Vozovna Střešovice",
    "limit": 6,
}

# Gets the data from the url with the given headers and parameters.
response = requests.get(url, headers=headers, params=parameters, timeout=15)
response.raise_for_status()

# Converts the data to python friendly formatting
data = response.json()

# Prints the data in an easily readable format.
# print(json.dumps(data, indent=2, ensure_ascii=False)) # ensure_ascii=False preserves the czech characters in normal format

# Assigns departures the array of departures
departures = data.get("departures", [])

#print(json.dumps(departures[2], indent=2, ensure_ascii=False))

for dep in departures:
    route_info = dep.get("route", {})
    trip_info = dep.get("trip", {})
    departure_info = dep.get("departure_timestamp", {})
    delay_info = dep.get("delay", {})

    line = str(route_info.get("short_name", ""))
    destination = trip_info.get("headsign", "")
    raw_dep_time = departure_info.get("predicted", "")
    delay_value = str(delay_info.get("minutes", ""))

    dt_dep_time = datetime.fromisoformat(raw_dep_time)
    final_dep_time = dt_dep_time.strftime("%H:%M")


    print(line + " | " + destination + " | " + str(final_dep_time) + " | + " + delay_value)





