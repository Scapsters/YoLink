from Interfaces.Responses.Response import ResponseData

class LockGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        state                (str)  : State of lock, ["locked", "unlocked"].
        battery              (int)  : Level of device's battery, 0 to 4 means empty to full.
        version              (str)  : Firmware Version of device.
        tz                   (int)  : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.state: str = data["state"]["state"]
        self.battery: int = data["state"]["battery"]
        self.version: str = data["version"]
        self.tz: int = data["tz"]    