#!/usr/bin/env python3
"""
Imports
"""
import requests
from datetime import datetime


if __name__ == '__main__':
    """
    First Launch
    """
    response = requests.get("https://api.spacexdata.com/v5/launches/upcoming")
    launches = response.json()

    launches_sorted = sorted(launches, key=lambda x: x['date_unix'])

    first_launch = launches_sorted[0]
    launch_name = first_launch['name']
    launch_date_unix = first_launch['date_unix']
    launch_date_local = datetime.utcfromtimestamp(launch_date_unix).strftime('%Y-%m-%d %H:%M:%S')
    rocket_name = first_launch['rocket']
    launchpad_id = first_launch['launchpad']

    launchpad_response = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")
    launchpad_data = launchpad_response.json()
    launchpad_name = launchpad_data['name']
    launchpad_locality = launchpad_data['locality']

    launch_info = f"{launch_name} ({launch_date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
    print(launch_info)
