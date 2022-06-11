from pydantic import BaseModel
from enum import Enum


class Color(Enum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"


class ColoredItemsBaseModel(BaseModel):
    color: Color

