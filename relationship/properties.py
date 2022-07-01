from dataclasses import dataclass
from typing import Dict, List

from relationship.feature_reference import FeatureReference


@dataclass
class Properties:
    category : str = None
    direction : str = None
    origin : FeatureReference = False
    intermediary : List[FeatureReference] = None
    destination : FeatureReference = None
    hours : str = None