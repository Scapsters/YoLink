from Interfaces.Responses.Response import ResponseData

class OutletGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        state                (str)  : State of device, ["closed", "open"].
        delay_on             (int)  : The remain time of Delay ON; Unit of minute; 0 is OFF.
        delay_off            (int)  : The remain time of Delay OFF; Unit of minute; 0 is OFF.
        power                (Optional[int]) : Current Power. If device does not support it, it will be 0.
        version              (str)  : Firmware Version of device.
        tz                   (int)  : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.state: str = data["state"]
        self.delay_on: int = data["delay"]["on"]
        self.delay_off: int = data["delay"]["off"]
        self.power: int | None = data.get("power")
        self.version: str = data["version"]
        self.tz: int = data["tz"]