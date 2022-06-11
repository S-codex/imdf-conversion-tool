from dataclasses import dataclass
from typing import Dict

from building.display_point import DisplayPoint


@dataclass
class Properties:
    name : Dict[str, str] = None
    alt_name : Dict[str, str] = None
    category : str = None
    restriction : str = None
    display_point : DisplayPoint = None
    address_id : str = None