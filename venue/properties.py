from dataclasses import dataclass
from typing import Dict, Optional

from venue.display_point import DisplayPoint


@dataclass
class Properties:
    category : str = None
    restriction : str = None
    name : Dict[str, str] = None
    alt_name : Dict[str, str] = None
    hours : str = None
    phone : str = None
    website : str = None
    display_point : DisplayPoint = None
    address_id : str = None