from typing import List
from Interfaces.Device import Device
from Interfaces.Responses.Response import ResponseData


class HubGetDeviceListData(ResponseData):
    """
    Represents the response of the Hub.getDeviceList method in the YoLink API.

    Attributes:
        devices (List[DeviceInfo]): List of devices connected to the hub.
    """

    def __init__(self, data: dict):
        self.devices: List[Device] = [Device(device) for device in data["devices"]] 
        
class HubGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        version                (str)  : Hub's Version.
        wifi_enable            (bool) : Is WiFi Connected.
        wifi_ssid              (str)  : Current connected Wi-Fi.
        wifi_ip                (str)  : Current IP of Wi-Fi.
        wifi_gateway           (str)  : Current Gateway of Wi-Fi.
        wifi_mask              (str)  : Current Subnet Mask of Wi-Fi.
        eth_enable             (bool) : Is Ethernet Connected.
        eth_ip                 (str)  : Current IP of Ethernet.
        eth_gateway            (str)  : Current Gateway of Ethernet.
        eth_mask               (str)  : Current Subnet Mask of Ethernet.
    """

    def __init__(self, data: dict):
        self.version: str = data["version"]
        self.wifi_enable: bool = data["wifi"]["enable"]
        self.wifi_ssid: str = data["wifi"]["ssid"]
        self.wifi_ip: str = data["wifi"]["ip"]
        self.wifi_gateway: str = data["wifi"]["gateway"]
        self.wifi_mask: str = data["wifi"]["mask"]
        self.eth_enable: bool = data["eth"]["enable"]
        self.eth_ip: str = data["eth"]["ip"]
        self.eth_gateway: str = data["eth"]["gateway"]
        self.eth_mask: str = data["eth"]["mask"]
