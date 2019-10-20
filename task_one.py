""" Module achieves below task

# Task 1

    The Star Wars API lists 87 main characters in the Star Wars saga. For the first task, we would
    like you to use a random number generator that picks a number between 1-87. Using these random
    numbers you will be pulling 15 characters from the API using Python.
"""

import requests
from enum import Enum
from random import randrange
from typing import List

from commons.dals import (
    print_characters,
    upsert_characters,
    get_people_film_mapping,
    upsert_films,
    upsert_people_film_rels,
    format_output
)


class Endpoints(Enum):
    """endpoints to be used throughout the script"""

    PEOPLE = "https://swapi.co/api/people/{}/"
    SPECIES = "https://swapi.co/api/species/{}/"
    VEHICLE = "https://swapi.co/api/vehicles/{}/"
    FILM = "https://swapi.co/api/films/{}/"
    STARSHIP = "https://swapi.co/api/starships/{}/"
    PLANET = "https://swapi.co/api/planets/{}/"


def _randset(start: int = 1, stop: int = 87, limit: int = 15) -> List[int]:
    """ creates a list of random integers in numerical range(start:stop)

    Args:
        start (int): first numeric value in range.
        stop (int): last numeric value in range.
        limit (int): number of results to yield.

    Returns:
        List[int]: random values in range(start:stop) with count limited to `limit`.
    """

    return [randrange(start, stop + 1) for i in range(limit)]


result = _randset(1, 87, 15)
# print(f"_randset(1, 87, 15) :: {result}\n\nwith length :: {len(result)}")


def fetch_all_rel_films(rel_films):
    """

    Args:
        rel_films (list): fetches all people-related films as listed.

    Returns:
        fetched_films (dict): film objects as received from swapi.

    """

    fetched_films = dict()

    for i in rel_films:
        endpoint = Endpoints.FILM.value.format(i)
        data = requests.get(endpoint)
        print(f"\ndata has been downloaded from {endpoint} - {data.json()}\n")
        fetched_films[endpoint] = data.json()
    return fetched_films


def fetch_all_rel_chars(peopleset):
    """

    Args:
        peopleset (list): fetches all people as ids listed in here.

    Returns:
        fetched_chars (dict): character objects as received from swapi.
    """

    fetched_chars = dict()

    for i in peopleset:
        endpoint = Endpoints.PEOPLE.value.format(i)
        data = requests.get(endpoint)
        print(f"\ndata has been downloaded from {endpoint} - {data.json()}\n")
        fetched_chars[endpoint] = data.json()

    return fetched_chars


def resolve_film_deps():
    people_film_list = get_people_film_mapping()

    people_film_map = {}
    all_rel_films = []
    for bundle in people_film_list:
        films = bundle["films"].split(" ")
        people_film_map[int(bundle["char_id"])] = [int(film) for film in films]
        all_rel_films.extend(films)

    fetched_films = fetch_all_rel_films(all_rel_films)
    print(f"\n\n\nfetched films here - {fetched_films}\n\n\n")

    for endpoint_, film_ in fetched_films.items():
        upsert_films(film_, endpoint_)

    upsert_people_film_rels(people_film_map)


if __name__ == "__main__":

    peopleset = _randset(1, 87, 15)

    fetched_chars = fetch_all_rel_chars(peopleset)

    print_characters()

    for endpoint_, char_ in fetched_chars.items():
        upsert_characters(char_, endpoint_)

    print("Pulling films of each character....!!! Another 2 mins, please wait!")
    resolve_film_deps()

    print("\n\nHmm!!! We are ready with random 15 people "
          "and all of their respective films in our database!!")

    print(f"\n\nEnter ID of character (aka people id) - \n[ CHOICES ]\n {peopleset}")

    try:
        people_id = int(input())
    except ValueError:
        print("[ ERROR ] Please enter numeric value from given choices")
    result = format_output(people_id)
    print(f"\n\nHere is list of films they worked in - \n\n{result}")
