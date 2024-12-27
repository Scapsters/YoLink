from Interfaces.Responses.Response import ResponseData

class MotionSensorGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        online               (bool)  : Is device online.
        state                (str)   : State of this device, ["normal", "alert"].
        battery              (str)   : Level of device's battery, 0 to 4 means empty to full.
        alertInterval        (Optional[int]) : Interval of Continuous Alert.
        ledAlarm             (Optional[bool]) : Is LED blink when motion detected.
        nomotionDelay        (Optional[int]) : Time to enter No-Motion state.
        version              (str)   : Firmware Version of device.
        reportAt             (str)   : Time of reported.
        deviceId             (str)   : ID of device.
    """

    def __init__(self, data: dict):
        self.online: bool = data["state"]["online"]
        self.state: str = data["state"]["state"]
        self.battery: str = data["state"]["battery"]
        self.alertInterval: int | None = data["state"].get("alertInterval")
        self.ledAlarm: bool | None = data["state"].get("ledAlarm")
        self.nomotionDelay: int | None = data["state"].get("nomotionDelay")
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"]   