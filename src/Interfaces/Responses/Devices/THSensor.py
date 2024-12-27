from Interfaces.Responses.Response import ResponseData

class THSensorGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        online               (bool) : Indicates if the device is online.
        state                (str)  : State of the device, can be "normal" or "alert".
        battery              (str)  : Level of the device's battery, 0 to 4 means empty to full.
        interval     (Optional[int]): Interval of Continuous Alert.
        temperature          (float): Current temperature.
        humidity             (float): Current humidity.
        tempLimit            (dict) : Normal temperature range, alert when temperature is out of it.
        humidityLimit        (float): Normal humidity range, alert when humidity is out of it.
        tempCorrection       (float): Calibration of temperature.
        humidityCorrection   (float): Calibration of humidity.
        version              (str)  : Firmware version of the device.
        reportAt             (str)  : Time of the report.
        deviceId             (str)  : ID of the device.
        interval is omitted due to it being optional in the documentation.
    """

    def __init__(self, data: dict):
        self.online: bool = data["online"]
        self.state: str = data["state"]["state"]
        self.battery: str = data["state"]["battery"]
        self.interval: int | None = data["state"].get("interval")
        self.temperature: float = data["state"]["temperature"]
        self.humidity: float = data["state"]["humidity"]
        self.tempLimit: dict = data["state"]["tempLimit"]
        self.humidityLimit: float = data["state"]["humidityLimit"]
        self.tempCorrection: float = data["state"]["tempCorrection"]
        self.humidityCorrection: float = data["state"]["humidityCorrection"]
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"]
