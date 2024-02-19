#!/usr/bin/env python3
"""
Imports
"""
import requests


def availableShips(passenger_count):
    """
    Get all avaliable ships that can hold a certian amount of passengers
    """
    url = 'https://swapi.dev/api/starships/'
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data['results']:
            if ship['passengers'].isnumeric():
                if int(ship['passengers']) >= passenger_count:
                    ships.append(ship['name'])

        url = data['next']

    return ships
