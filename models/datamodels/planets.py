"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from decimal import Decimal
from models.basemodel import Base


class Planet(Base):
    """ Pydantic model class meant to validate the data for `Planet` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str

    # Relationship attribute fields
    films: Optional[List[str]]
    residents: Optional[List[str]]

