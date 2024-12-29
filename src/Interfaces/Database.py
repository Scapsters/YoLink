from abc import ABC, abstractmethod
from collections import OrderedDict

class Database(ABC):
    
    @abstractmethod
    def save(self, device_type: str, header: OrderedDict[str, str|int]) -> None:
        '''
        Save the header to a file of the given device type.
        
        Args:
            device_type (str): The type of device.
            header (OrderedDict[str, str|int]): The header to save.
        '''
        pass
    
    @abstractmethod
    def add_device(self, device_id, device_name, device_type, timestamp) -> None:
        pass
