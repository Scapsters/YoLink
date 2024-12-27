from Interfaces.Responses.Response import ResponseData

class DoorSensorGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        online               (bool)  : Is device online.
        state                (str)   : State of this device, ["closed", "open", "error"].
        battery              (str)   : Level of device's battery, 0 to 4 means empty to full.
        openRemindDelay      (Optional[int]) : When device is still open past this time, an OpenRemind event triggered.
        alertInterval        (Optional[int]) : Interval of Continuous Alert.
        version              (str)   : Firmware Version of device.
        reportAt             (str)   : Time of reported.
        deviceId             (str)   : ID of device.
    """

    def __init__(self, data: dict):
        self.online: bool = data["state"]["online"]
        self.state: str = data["state"]["state"]
        self.battery: str = data["state"]["battery"]
        self.openRemindDelay: int | None = data["state"].get("openRemindDelay")
        self.alertInterval: int | None = data["state"].get("alertInterval")
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"]
