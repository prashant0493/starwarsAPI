"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from decimal import Decimal
from models.basemodel import Base


class Species(Base):
    """ Pydantic model class meant to validate the data for `Species` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    average_height: str
    average_lifespan: str
    classification: str
    designation: str
    eye_colors: str
    hair_colors: str
    homeworld: Optional[str]
    language: str
    name: str
    skin_colors: str

    # relationship attribute fields
    people: Optional[List[str]]
    films: Optional[List[str]]
