#!/usr/bin/env python3
"""
Imports
"""
import requests


def sentientPlanets():
    """
    Get a list of all the names of home planets of the sentient species
    """
    url = 'https://swapi.dev/api/species/'
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data['results']:
            if ('classification' in species and
                species['classification'].lower() == 'sentient') or \
               ('designation' in species and
               species['designation'].lower() == 'sentient'):
                    if 'homeworld' in species and species['homeworld']:
                        homeworld_url = species['homeworld']
                        homeworld_response = requests.get(homeworld_url)
                        homeworld_data = homeworld_response.json()
                        planets.append(homeworld_data['name'])

        url = data['next']

    return planets
