class Device():
    """
    Represents the information of a device in the YoLink API.

    Attributes:
        deviceId    (str) : The DeviceId.
        deviceUUID  (str) : The device's UUID.
        token       (str) : The device's net token; It's necessary when you send a message to this device.
        name        (str) : Device's product name.
        type        (str) : Device's type name; Such as 'Hub', could call method <Hub.*> with this device.
    """

    def __init__(self, data: dict):
        self.deviceId: str = data["deviceId"]
        self.deviceUUID: str = data["deviceUUID"]
        self.token: str = data["token"]
        self.name: str = data["name"]
        self.type: str = data["type"]

