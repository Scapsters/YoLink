class Device():
    """
    Represents the information of a device in the YoLink API.

    Attributes:
        device_id   (str) : The DeviceId.
        device_udid (str) : The device's UDID.
        token       (str) : The device's net token; It's necessary when you send a message to this device.
        name        (str) : Device's product name.
        type        (str) : Device's type name; Such as 'Hub', could call method <Hub.*> with this device.
    """

    def __init__(self, data: dict):
        self.device_id   = data["deviceId"]
        self.device_udid = data["deviceUDID"]
        self.token       = data["token"]
        self.name        = data["name"]
        self.type        = data["type"]

