from dataclasses import dataclass
from typing import List


@dataclass
class DisplayPoint:
    type : str = "Point"
    coordinates : List[float] = None