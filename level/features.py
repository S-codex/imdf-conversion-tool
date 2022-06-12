from dataclasses import dataclass

from level.geometry import Geometry
from level.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "level"
    geometry: Geometry = None
    properties: Properties = None