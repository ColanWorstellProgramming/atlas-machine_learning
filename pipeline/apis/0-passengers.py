#!/usr/bin/env python3
"""
Imports
"""
import requests


def availableShips(passenger_count):
    """
    Get all avaliable ships that can hold a certian amount of passengers
    """
    ships = []
    page = 1
    url = 'https://swapi.dev/api/starships/?page={}'.format(page)

    response = requests.get(url)
    data = response.json()

    while data['next']:
        for ship in data['results']:

            if ship['passengers'] == 'n/a':
                continue
            if ship['passengers'] == 'unknown':
                continue
            if int(ship['passengers'].replace(',', '')) >= passenger_count:
                ships.append(ship['name'])

        page += 1
        url = 'https://swapi.dev/api/starships/?page={}'.format(page)
        response = requests.get(url)
        data = response.json()

    return ships
