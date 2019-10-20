"""Maintains list of constants required across project"""

from enum import Enum


class Endpoints(Enum):
    """endpoints to be used throughout the script"""

    PEOPLE = "https://swapi.co/api/people/{}/"
    SPECIES = "https://swapi.co/api/species/{}/"
    VEHICLE = "https://swapi.co/api/vehicles/{}/"
    FILM = "https://swapi.co/api/films/{}/"
    STARSHIP = "https://swapi.co/api/starships/{}/"
    PLANET = "https://swapi.co/api/planets/{}/"
