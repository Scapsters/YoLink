from Interfaces.Responses.Response import ResponseData

class SpeakerHubGetStateData(ResponseData):
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
        options_volume         (int)  : Global volume of device.
        options_enableBeep     (bool) : Is beep enabled. True means the device will make a beep when performing some actions, such as startup, modify settings.
        options_mute           (bool) : Is mute mode enabled. True means device will not make any sound, even if you receive a message.
    """

    def __init__(self, data: dict):
        self.version: str = data["version"]
        self.wifi_enable: bool = data["wifi"]["enable"]
        self.wifi_ssid: str = data["wifi"]["ssid"]
        self.wifi_ip: str = data["wifi"]["ip"]
        self.wifi_gateway: str = data["wifi"]["gateway"]
        self.wifi_mask: str = data["wifi"]["mask"]
        self.eth_enable: bool = data["eth"]["enable"]
        self.options_volume: int = data["options"]["volume"]
        self.options_enableBeep: bool = data["options"]["enableBeep"]
        self.options_mute: bool = data["options"]["mute"] 