""" Module achieves below task

# Task 1

    The Star Wars API lists 87 main characters in the Star Wars saga. For the first task, we would
    like you to use a random number generator that picks a number between 1-87. Using these random
    numbers you will be pulling 15 characters from the API using Python.
"""

import requests
from random import randrange
from typing import List, Dict

from commons.dals import (
    # print_character,
    upsert_characters,
    get_people_film_mapping,
    upsert_films,
    upsert_people_film_rels,
    format_output
)
from commons.constants import Endpoints


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


def fetch_all_rel_films(rel_films) -> Dict:
    """fetches all people related films as listed in param `rel_films`.

    Args:
        rel_films (list): fetches all people-related films as listed.

    Returns:
        fetched_films (dict): film objects as received from swapi.

    """

    fetched_films = dict()

    for i in rel_films:
        endpoint = Endpoints.FILM.value.format(i)
        data = requests.get(endpoint)
        # print(f"\ndata has been downloaded from {endpoint} - {data.json()}\n")
        print(f"\n-- data has been downloaded from ```{endpoint}``` --")
        fetched_films[endpoint] = data.json()
    return fetched_films


def fetch_all_rel_chars(peopleset) -> Dict:
    """fetches all characters as listed in param `peopleset`

    Args:
        peopleset (list): fetches all people as ids listed in here.

    Returns:
        fetched_chars (dict): character objects as received from swapi.
    """

    fetched_chars = dict()

    for i in peopleset:
        endpoint = Endpoints.PEOPLE.value.format(i)
        data = requests.get(endpoint)
        # print(f"\ndata has been downloaded from {endpoint} - {data.json()}\n")
        print(f"\n-- data has been downloaded from ```{endpoint}``` --")
        fetched_chars[endpoint] = data.json()

    return fetched_chars


def resolve_film_deps() -> None:
    """Resolves dependecies for all the `character` entities existing in the database and inserts
        values into table `film` and table `CharFilmRelation`.

    Returns: None

    """
    people_film_list = get_people_film_mapping()

    people_film_map = {}
    all_rel_films = []
    for bundle in people_film_list:
        films = bundle["films"].split(" ")
        people_film_map[int(bundle["char_id"])] = [int(film) for film in films]
        all_rel_films.extend(films)

    fetched_films = fetch_all_rel_films(all_rel_films)
    # print(f"\n\n\nfetched films here - {fetched_films}\n\n\n")

    for endpoint_, film_ in fetched_films.items():
        upsert_films(film_, endpoint_)

    upsert_people_film_rels(people_film_map)


if __name__ == "__main__":

    # generates list of random ids. Usage ```_randset(start, end, limit)```
    peopleset = _randset(1, 87, 15)
    print(f"\n[ NOTE ] LIST OF RANDOM PEOPLE IDs"
          f" (as selected by random number generator) :: \n\n{peopleset}\n")

    fetched_chars = fetch_all_rel_chars(peopleset)
    # print_characters()

    # inserts/updates each fetched character into database.
    for endpoint_, char_ in fetched_chars.items():
        upsert_characters(char_, endpoint_)

    print("\n\n[ NOTE ] Pulling films of each character....!!! Another 2 mins, please wait!")

    # gets respective films for each character and stores into relationship table in database.
    resolve_film_deps()

    print(f"\n\nHmm!!! We are ready with random 15 people ",
          f"and all of their respective films in our database!!",
          f"\n\nEnter ID of character (aka people id) - \n[ CHOICES ]\n {peopleset}")

    try:
        people_id = int(input())
    except ValueError:
        print("[ ERROR ] Please enter numeric value from given choices")

    # formats result into required format as per task 1
    result = format_output(people_id)
    print(f"\n\nHere is list of films they worked in - \n\n{result}")
