from dataclasses import dataclass
from typing import List

from building.features import Features


@dataclass
class Building:
    type: str = None
    name: str = None
    features: List[Features] = None
