"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List
from decimal import Decimal
from datetime import date
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
    release_date: date

    # relationship attribute fields
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
