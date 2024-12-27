from Interfaces.Responses.Response import ResponseData

class MultiOutletGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        state                (list[str]) : State of device's sockets, ["closed", "open"].
        delays_on            (int)       : The remain time of Delay ON; Unit of minute; 0 is OFF.
        delays_off           (int)       : The remain time of Delay OFF; Unit of minute; 0 is OFF.
        version              (str)       : Firmware Version of device.
        tz                   (int)       : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.state: list[str] = data["state"]
        self.delays_on: int = data["delays"][0]["on"]
        self.delays_off: int = data["delays"][0]["off"]
        self.version: str = data["version"]
        self.tz: int = data["tz"] 