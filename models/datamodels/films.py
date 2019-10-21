"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from models.basemodel import Base


class Film(Base):
    """ Pydantic model class meant to validate the data for `Film` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    title: str
    episode_id: str
    opening_crawl: str
    director: str
    producer: str
    release_date: str

    # relationship attribute fields
    characters: Optional[List[str]]
    planets: Optional[List[str]]
    starships: Optional[List[str]]
    vehicles: Optional[List[str]]
    species: Optional[List[str]]
