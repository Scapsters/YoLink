from Interfaces.Responses.Response import ResponseData

class InfraredRemoterGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        battery    (int)        : Battery Level (1 ~ 4), 1 is empty and 4 is full.
        keys       (list[bool]) : 64 keys, true means this key is learned.
        version    (str)        : Firmware Version.
        tz         (int)        : Timezone of this device.
    """

    def __init__(self, data: dict):
        self.battery: int = data["battery"]
        self.keys: list[bool] = data["keys"]
        self.version: str = data["version"]
        self.tz: int = data["tz"]