from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[str]
    first_name: str
    last_name: str
    email: str
    password: str
    username: str
