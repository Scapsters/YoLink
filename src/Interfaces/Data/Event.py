from pydantic.dataclasses import dataclass
from typing import List
from Interfaces.Data.DataEntry import DataEntry

@dataclass
class Event():
    data_entries: List[DataEntry]
    source_device_id: str
    timestamp: str
    