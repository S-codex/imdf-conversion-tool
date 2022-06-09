from dataclasses import dataclass

from venue.geometry import Geometry
from venue.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "venue"
    geometry: Geometry = None
    properties: Properties = None