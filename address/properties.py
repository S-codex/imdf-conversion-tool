from dataclasses import dataclass

@dataclass
class Properties:
    address : str = None
    unit : str = None
    locality : str = None
    province : str = None
    country : str = None
    postal_code : str = None
    postal_code_ext : str = None
    postal_code_vanity : str = None