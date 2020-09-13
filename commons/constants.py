"""Maintains list of constants required across project"""

from enum import Enum


class Endpoints(Enum):
    """endpoints to be used throughout the script"""

    PEOPLE = "https://swapi.dev/api/people/{}/"
    SPECIES = "https://swapi.dev/api/species/{}/"
    VEHICLE = "https://swapi.dev/api/vehicles/{}/"
    FILM = "https://swapi.dev/api/films/{}/"
    STARSHIP = "https://swapi.dev/api/starships/{}/"
    PLANET = "https://swapi.dev/api/planets/{}/"
