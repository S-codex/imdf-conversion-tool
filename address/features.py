from dataclasses import dataclass

from address.properties import Properties


@dataclass
class Features:
    type: str = "Feature"
    id: str = None
    feature_type: str = "address"
    geometry: str = None
    properties: Properties = None