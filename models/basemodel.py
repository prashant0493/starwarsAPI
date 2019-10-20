"""
This module defines pydantic basemodel (provides Py3 data-classes validation out of the box)
used for common fields and methods used across all the datamodels.
"""

from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):

    created: datetime
    edited: datetime
    url: str
