from typing import List
from Interfaces.Device import Device
from Interfaces.Responses.Response import ResponseData

class HomeGetDeviceListData(ResponseData):
    """
    Represents the response of the Home.getDeviceList method in the YoLink API.

    Attributes:
        devices (List[DeviceInfo]): List of devices connected to the hub.
    """

    def __init__(self, data: dict):
        self.devices = [Device(device) for device in data["devices"]]
        
    def print_data(self):
        return 
