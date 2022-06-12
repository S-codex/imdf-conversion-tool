from dataclasses import dataclass
from typing import Dict

from level.display_point import DisplayPoint


@dataclass
class Properties:
    category : str = None
    restriction : str = None
    outdoor : bool = False
    ordinal : int = 0
    name : Dict[str, str] = None
    short_name : Dict[str, str] = None
    display_point : DisplayPoint = None
    address_id : str = None
    building_ids : str = None