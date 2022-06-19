from dataclasses import dataclass
from typing import List

from opening.features import Features


@dataclass
class Opening:
    type: str = None
    name: str = None
    features: List[Features] = None
