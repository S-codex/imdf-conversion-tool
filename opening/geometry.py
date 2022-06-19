from dataclasses import dataclass
from typing import List


@dataclass
class Geometry:
    type: str = "LineString"
    coordinates: List[List[float]] = None
