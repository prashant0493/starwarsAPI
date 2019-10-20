"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from decimal import Decimal
from typing import List
from models.basemodel import Base


class Vehicle(Base):
    """ Pydantic model class meant to validate the data for `Vehicle` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: int
    length: Decimal
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: int
    vehicle_class: str

    # relationship attribute fields
    pilots: List[str]
    films: List[str]
