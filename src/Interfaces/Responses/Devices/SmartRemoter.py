from Interfaces.Responses.Response import ResponseData

class SmartRemoterGetStateData(ResponseData):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        event                (Optional[dict]) : The last reported event.
        event_keyMask        (Optional[int])            : Triggered keys of event. Bits 0-7 means keys 0-7.
        event_type           (Optional[str])            : The type of event, ["Press", "LongPress"].
        battery              (int)            : Level of device's battery, 0 to 4 means empty to full.
        version              (str)            : Firmware Version of device.
        reportAt             (str)            : Time of reported.
        deviceId             (str)            : ID of device.
    """

    def __init__(self, data: dict):
        self.event: dict | None = data["state"].get("event")
        self.event_keyMask: int | None = data["state"]["event"]["keyMask"] if self.event else None
        self.event_type: str | None = data["state"]["event"]["type"] if self.event else None
        self.battery: int = data["state"]["battery"]
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"] 