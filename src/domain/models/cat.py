from dataclasses import dataclass
from typing import Optional

@dataclass
class CatBreed:
    id: str
    name: str
    origin: Optional[str] = None
    description: Optional[str] = None
    temperament: Optional[str] = None
