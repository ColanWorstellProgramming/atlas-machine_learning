#!/usr/bin/env python3
"""
Imports
"""
import requests


if __name__ == '__main__':
    """
    Rocket Frequency
    """
    response = requests.get("https://api.spacexdata.com/v3/launches")
    launches = response.json()

    rocket_launch_counts = {}

    for launch in launches:
        rocket_name = launch['rocket']['rocket_name']
        rocket_launch_counts[rocket_name] = rocket_launch_counts.get(rocket_name, 0) + 1

    sorted_rocket_launch_counts = sorted(rocket_launch_counts.items(), key=lambda x: (-x[1], x[0]))

    for rocket_name, launch_count in sorted_rocket_launch_counts:
        print(f"{rocket_name}: {launch_count}")
