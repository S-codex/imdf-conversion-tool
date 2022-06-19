from dataclasses import dataclass


@dataclass
class Door:
    automatic: bool = None
    material: str = None
    type: str = None
