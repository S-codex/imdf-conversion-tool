from dataclasses import dataclass

from building.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "building"
    geometry: str = None
    properties: Properties = None