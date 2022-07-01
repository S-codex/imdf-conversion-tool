from dataclasses import dataclass

from unit.geometry import Geometry
from unit.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "unit"
    geometry: Geometry = None
    properties: Properties = None