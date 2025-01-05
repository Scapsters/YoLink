from pydantic.dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class DataEntry(Generic[T]):
    name: str
    value: T