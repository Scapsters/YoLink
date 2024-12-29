from pydantic.dataclasses import dataclass
from typing import TypeVar, Generic
from Interfaces.Data.Event import Event

T = TypeVar('T')

class DataEntry(dataclass, Generic[T]):
    event_id: int
    name: str
    value: T
    event: Event