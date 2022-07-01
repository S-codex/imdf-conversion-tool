from dataclasses import dataclass
from typing import Dict, List

from unit.display_point import DisplayPoint


@dataclass
class Properties:
    category : str = None
    restriction : str = None
    accessibility: List[str] = None
    name : Dict[str, str] = None
    alt_name : Dict[str, str] = None
    level_id : str = None
    display_point : DisplayPoint = None