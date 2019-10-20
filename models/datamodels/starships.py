"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List
from decimal import Decimal
from models.basemodel import Base


class Starship(Base):
    """ Pydantic model class meant to validate the data for `Starship` object from single resource
        endpoint from starwars API.
    """

    # attribute fields
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: int
    hyperdrive_rating: str
    length: Decimal
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    starship_class: str
    passengers: str

    # relationship attribute fields
    films: List[str]
    pilots: List[str]
