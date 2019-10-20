"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List
from decimal import Decimal
from models.basemodel import Base


class Character(Base):
    """ Pydantic model class meant to validate the data for `Character` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str

    # relationship attribute fields
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]









