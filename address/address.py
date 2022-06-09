from dataclasses import dataclass
from typing import List

from address.features import Features


@dataclass
class Address:
    type: str = None
    name: str = None
    features: List[Features] = None
