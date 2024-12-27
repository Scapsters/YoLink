from Interfaces.Responses.Response import ResponseData

class ManipulatorGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        state                (str)  : Current state of device, ["closed", "open"].
        delay_on             (Optional[int]) : The remain time of Delay ON; Unit of minute; 0 is OFF.
        delay_off            (Optional[int]) : The remain time of Delay OFF; Unit of minute; 0 is OFF.
        openRemind           (Optional[int]) : Time to remind when device keeps open. 0 is disabled.
        version              (str)  : Firmware Version of device.
        tz                   (int)  : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.state: str = data["state"]
        self.delay_on: int | None = data["delay"].get("on")
        self.delay_off: int | None = data["delay"].get("off")
        self.openRemind: int | None = data.get("openRemind")
        self.version: str = data["version"]
        self.tz: int = data["tz"]  