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

# Assigns departures the array of departures
departures = data.get("departures", [])

# Prints the data in an easily readable format.
# print(json.dumps(departures[2], indent=2, ensure_ascii=False)) # ensure_ascii=False preserves the czech characters in normal format

# Prints the desired format for each of the requested departures.
for dep in departures:
    # Assigns the dictionary values while protecting against empty values.
    route_info = dep.get("route") or {}
    trip_info = dep.get("trip") or {}
    departure_info = dep.get("departure_timestamp") or {}
    delay_info = dep.get("delay") or {}

    line = str(route_info.get("short_name")) or ""
    destination = trip_info.get("headsign") or ""
    raw_dep_time = departure_info.get("predicted") or ""
    delay_value = str(delay_info.get("minutes")) or ""

    # Checks whether the predicted departure time is present. If not, it switches to scheduled departure.
    if raw_dep_time == "":
        raw_dep_time = departure_info.get("scheduled") or ""

        # Checks whether the scheduled departure time is present.
        if raw_dep_time == "":
            print("Error. There is no departure time given!")
        else:
            dt_dep_time = datetime.fromisoformat(raw_dep_time)
            final_dep_time = dt_dep_time.strftime("%H:%M")
            final_print = line + " | " + destination + " | " + str(final_dep_time) + " | " + delay_value
    else:
        dt_dep_time = datetime.fromisoformat(raw_dep_time)
        final_dep_time = dt_dep_time.strftime("%H:%M")
        final_print = line + " | " + destination + " | " + str(final_dep_time) + " | " + delay_value

    # Checks whether the delay value is present. If not, it doesn't show the delay part.
    if delay_value == "":
        final_print = line + " | " + destination + " | " + str(final_dep_time)
    else:
        final_print = line + " | " + destination + " | " + str(final_dep_time) + " | " + delay_value


    print(final_print)
