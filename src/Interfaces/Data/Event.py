from pydantic.dataclasses import dataclass
from typing import List
from Interfaces.Data.DataEntry import DataEntry

class Event(dataclass):
    data_entries: List[DataEntry]
    timestamp: str