"""The task 2 goes like following:

1. Pull data for the movie ​A New Hope

2. Replace the data for each of the endpoints listed in the JSON object you
   receive from the API request (e.g. - In the example above you would take
   all the character endpoints and pull the data from each of those
   endpoints then insert the data into the JSON object, etc.)
        a. A New Hope​ has character, planet, starship, vehicle, and species
           data you will need to retrieve and replace.

3. We also ask that you convert the metric heights and weights of each
   character to standard units.

4. You will also need to remove all cross-referencing material from the
   data you replace (e.g. - When you pull Luke Skywalker you would want
   to remove cross-referencing URLs from Luke’s JSON object (like films,
   species, vehicles, and spaceships.)

5. Lastly, you will take the dictionary you created and write it out to
   a JSON file locally named ​task_two.json.​
"""

import requests
import os
from typing import Dict, List, Optional
from commons.constants import Endpoints

from models.datamodels.films import Film
from models.datamodels.characters import Character
from models.datamodels.starships import Starship
from models.datamodels.vehicles import Vehicle
from models.datamodels.planets import Planet
from models.datamodels.species import Species
from models.datamodels.response_model import Final

from multiprocessing.pool import ThreadPool


def fetch_film(film_id) -> Dict:
    """fetches film object using film_id param

    Args:
        film_id (int): fetches all people as ids listed in here.

    Returns:
        fetched_film (dict): film object as received from swapi.
    """

    endpoint = Endpoints.FILM.value.format(film_id)
    data = requests.get(endpoint)
    # print(f"\ndata has been downloaded from {endpoint} - {data.json()}\n")
    print(f"\n-- data has been downloaded from ```{endpoint}``` --")
    return data.json()


def fetch_endpoint(url):
    data = requests.get(url)

    if data.status_code == 404:
        return None

    return data.json()


def remove_cross_referencing_urls(resolved_objs: Optional[List]) -> None:
    """Uses relationship attribute list and removes those attributes from serialized object

    Args:
        resolved_objs (list):

    Returns:

    """

    rel_attrs = ["people", "films", "characters", "planets", "starships", "vehicles", "species"]

    if resolved_objs is None:
        pass

    for obj_ in resolved_objs:
        for rel_attr in rel_attrs:
            attr_ = getattr(obj_, rel_attr, None)
            if attr_ and isinstance(attr_, list):
                delattr(obj_, rel_attr)


def resolve_rels(urls, rel_attr) -> Optional[List]:
    """ fetches data from cross-referencing urls in the relationship fields
    Args:
        urls (list): list of urls to be resolved by removing cross-references.
        rel_attr (str): relationship field for reference.

    Returns:
        returns serialized version of resolved objects.
    """

    # create a thread-pool, to resolve IO-intensive operation real quick.
    pool = ThreadPool(5)
    results = pool.map(fetch_endpoint, urls)

    # some endpoints may NOT yield results (i.e. 404s Not Found.)
    if not results:
        return None

    resolved_objs = None

    # process objects through data-class validation
    if rel_attr == "characters":
        resolved_objs = [Character(**result) for result in results]
    elif rel_attr == "vehicles":
        resolved_objs = [Vehicle(**result) for result in results]
    elif rel_attr == "starships":
        resolved_objs = [Starship(**result) for result in results]
    elif rel_attr == "planets":
        resolved_objs = [Planet(**result) for result in results]
    elif rel_attr == "species":
        resolved_objs = [Species(**result) for result in results]
    else:
        pass

    remove_cross_referencing_urls(resolved_objs)

    return resolved_objs


def format_output(film: Film, resolutions: Dict) -> str:
    """formats standard JSON output as required

    Args:
        film:
        resolutions:

    Returns:

    """

    final = film.dict()
    final["characters"] = [obj_.dict() for obj_ in resolutions["characters"]]
    final["vehicles"] = [obj_.dict() for obj_ in  resolutions["vehicles"]]
    final["species"] = [obj_.dict() for obj_ in resolutions["species"]]
    final["planets"] = [obj_.dict() for obj_ in  resolutions["planets"]]
    final["starships"] = [obj_.dict() for obj_ in  resolutions["starships"]]

    final = Final(**final)
    return final.json()


if __name__ == "__main__":

    # pulling data from specific film as per task.
    print("\n\n[ NOTE ] Pulling data for the movie ``A new hope`` (film id: 1)")
    fetched_film = fetch_film(1)
    film = Film(**fetched_film)

    # pulling data for all relationship fields in the film json object.
    rel_attrs_for_film = ["characters", "planets", "starships", "vehicles", "species"]
    resolutions = {}
    for rel_attr in rel_attrs_for_film:
        attrs_ = getattr(film, rel_attr, None)
        resolved_objs_ = resolve_rels(attrs_, rel_attr)
        resolutions.setdefault(rel_attr, resolved_objs_)

    # formats the output to produce JSON as required.
    output = format_output(film, resolutions)

    # store output at current workdir of project with file name `task_two.json`
    filename = os.path.dirname(os.path.realpath(__file__)) + "/task_two.json"
    with open(filename, 'w') as foo:
        foo.write(output)

    print(f"[ SUCCESS ] The output JSON has been stored here - {filename}")

