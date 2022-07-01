from dataclasses import dataclass
from typing import List

from relationship.features import Features


@dataclass
class Relationship:
    type: str = None
    name: str = None
    features: List[Features] = None
