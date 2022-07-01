from dataclasses import dataclass
from typing import List

from unit.features import Features


@dataclass
class Unit:
    type: str = None
    name: str = None
    features: List[Features] = None
