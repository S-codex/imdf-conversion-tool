from dataclasses import dataclass
from typing import Dict, List

from opening.door import Door
from opening.display_point import DisplayPoint


@dataclass
class Properties:
    category: str = None
    accessibility: List[str] = None
    access_control: List[str] = None
    door: Door = None
    name: Dict[str, str] = None
    alt_name: Dict[str, str] = None
    display_point: DisplayPoint = None
    level_id: str = None
