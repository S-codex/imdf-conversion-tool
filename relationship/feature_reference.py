from dataclasses import dataclass


@dataclass
class FeatureReference:
    feature_type: str = None
    id: str = None
