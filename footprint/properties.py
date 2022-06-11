from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Properties:
    name: Dict[str, str] = None
    category: str = None
    building_ids: List[str] = None
