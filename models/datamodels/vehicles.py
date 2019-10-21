"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from models.basemodel import Base


class Vehicle(Base):
    """ Pydantic model class meant to validate the data for `Vehicle` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: int
    vehicle_class: str

    # relationship attribute fields
    pilots: Optional[List[str]]
    films: Optional[List[str]]
