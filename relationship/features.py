from dataclasses import dataclass

from relationship.geometry import Geometry
from relationship.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "relationship"
    geometry: Geometry = None
    properties: Properties = None