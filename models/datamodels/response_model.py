"""
This module defines pydantic (provides Py3 data-classes validation out of the box) model used
for de-serialization in API responses. Specifically for Task 2
"""

from typing import List, Optional
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


class Starship(Base):
    """ Pydantic model class meant to validate the data for `Starship` object from single resource
        endpoint from starwars API.
    """

    # attribute fields
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    starship_class: str
    passengers: str


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


class Final(Base):
    """ Pydantic model class meant to validate the data for `Final` object
    """

    # attribute fields
    title: str
    episode_id: str
    opening_crawl: str
    director: str
    producer: str
    release_date: str

    # relationship attribute fields
    characters: Optional[List[Character]]
    planets: Optional[List[Planet]]
    starships: Optional[List[Starship]]
    vehicles: Optional[List[Vehicle]]
    species: Optional[List[Species]]









