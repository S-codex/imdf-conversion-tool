from dataclasses import dataclass
from typing import List

from venue.features import Features


@dataclass
class Venue:
    type: str = None
    name: str = None
    features: List[Features] = None
