class Device():
    """
    Represents the information of a device in the YoLink API.

    Attributes:
        deviceId    (str) : The DeviceId.
        deviceUDID  (str) : The device's UDID.
        token       (str) : The device's net token; It's necessary when you send a message to this device.
        name        (str) : Device's product name.
        type        (str) : Device's type name; Such as 'Hub', could call method <Hub.*> with this device.
    """

    def __init__(self, data: dict):
        print(data)
        self.deviceId: str = data["deviceId"]
        self.deviceUUID: str = data["deviceUDID"]
        self.token: str = data["token"]
        self.name: str = data["name"]
        self.type: str = data["type"]

