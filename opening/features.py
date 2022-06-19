from dataclasses import dataclass

from opening.geometry import Geometry
from opening.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "opening"
    geometry: Geometry = None
    properties: Properties = None
