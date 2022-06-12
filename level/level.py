from dataclasses import dataclass
from typing import List

from level.features import Features


@dataclass
class Level:
    type: str = None
    name: str = None
    features: List[Features] = None
