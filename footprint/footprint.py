from dataclasses import dataclass
from typing import List

from footprint.features import Features


@dataclass
class Footprint:
    type: str = None
    name: str = None
    features: List[Features] = None
