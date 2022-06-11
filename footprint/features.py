from dataclasses import dataclass

from footprint.geometry import Geometry
from footprint.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "footprint"
    geometry: Geometry = None
    properties: Properties = None