from dataclasses import dataclass
from typing import List

@dataclass
class Geometry:
    type : str = "Polygon"
    coordinates : List[List[List[float]]] = None