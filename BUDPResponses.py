from abc import ABC, abstractmethod

class BUDPResponse(ABC):
    """
    Abstract class for BUDP responses of various sensor types.
    """

    @abstractmethod
    def __init__(self, data: dict):
        pass

class THSensorGetStateData(BUDPResponse):
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
        self.online: bool = data["state"]["online"]
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

class WaterMeterControllerGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        valve                       (str)  : Valve state, ["close","open"].
        meter                       (int)  : Meter reading.
        waterFlowing                (bool) : Water flowing.
        openReminder                (bool) : Open remind alarm.
        leak                        (bool) : Leak alarm.
        amountOverrun               (bool) : Amount overrun alarm.
        durationOverrun             (bool) : Duration overrun alarm.
        valveError                  (bool) : Valve error alarm.
        reminder                    (bool) : Remind repeat.
        freezeError                 (bool) : Freeze alarm.
        battery                     (int)  : Level of device's battery, 0 to 4 means empty to full.
        powerSupply                 (str)  : Power supply, ["battery","PowerLine"].
        valveDelay_on               (Optional[int]) : The remain time of Delay ON; Unit of minute; 0 is OFF.
        valveDelay_off              (Optional[int]) : The remain time of Delay OFF; Unit of minute; 0 is OFF.
        openReminder_duration       (int)  : Open remind duration in minute.
        meterUnit                   (int)  : Meter screen unit, 0-GAL 1-CCF 2-M3 3-L.
        alertInterval               (int)  : Alert interval in minute.
        meterStepFactor             (int)  : Meter measurement accuracy.
        leakLimit                   (float): Leak limit in meter unit.
        autoCloseValve              (bool) : Close valve if leak limit exceeded.
        overrunAmountACV            (bool) : Overrun amount auto close valve.
        overrunDurationACV          (bool) : Overrun duration auto close valve.
        leakPlan                    (str)  : Leak plan mode, ["on","off","schedule"].
        overrunAmount               (float): Overrun amount in meter unit.
        overrunDuration             (int)  : Overrun duration in minute.
        freezeTemp                  (float): Freeze temperature in celsius.
        recentUsage_amount          (int)  : Recent usage in meter unit.
        recentUsage_duration        (int)  : Recent usage duration in minute.
        dailyUsage                  (int)  : Daily usage in meter unit.
        temperature                 (float): Temperature in celsius.
        version                     (str)  : Firmware version.
        tz                          (int)  : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.valve: str = data["state"]["valve"]
        self.meter: int = data["state"]["meter"]
        self.waterFlowing: bool = data["state"]["waterFlowing"]
        self.openReminder: bool = data["alarm"]["openReminder"]
        self.leak: bool = data["alarm"]["leak"]
        self.amountOverrun: bool = data["alarm"]["amountOverrun"]
        self.durationOverrun: bool = data["alarm"]["durationOverrun"]
        self.valveError: bool = data["alarm"]["valveError"]
        self.reminder: bool = data["alarm"]["reminder"]
        self.freezeError: bool = data["alarm"]["freezeError"]
        self.battery: int = data["battery"]
        self.powerSupply: str = data["powerSupply"]
        self.valveDelay_on: int | None = data["valveDelay"].get("on")
        self.valveDelay_off: int | None = data["valveDelay"].get("off")
        self.openReminder_duration: int = data["attributes"]["openReminder"]
        self.meterUnit: int = data["attributes"]["meterUnit"]
        self.alertInterval: int = data["attributes"]["alertInterval"]
        self.meterStepFactor: int = data["attributes"]["meterStepFactor"]
        self.leakLimit: float = data["attributes"]["leakLimit"]
        self.autoCloseValve: bool = data["attributes"]["autoCloseValve"]
        self.overrunAmountACV: bool = data["attributes"]["overrunAmountACV"]
        self.overrunDurationACV: bool = data["attributes"]["overrunDurationACV"]
        self.leakPlan: str = data["attributes"]["leakPlan"]
        self.overrunAmount: float = data["attributes"]["overrunAmount"]
        self.overrunDuration: int = data["attributes"]["overrunDuration"]
        self.freezeTemp: float = data["attributes"]["freezeTemp"]
        self.recentUsage_amount: int = data["recentUsage"]["amount"]
        self.recentUsage_duration: int = data["recentUsage"]["duration"]
        self.dailyUsage: int = data["dailyUsage"]
        self.temperature: float = data["temperature"]
        self.version: str = data["version"]
        self.tz: int = data["tz"]

class DoorSensorGetStateData(BUDPResponse):
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

class InfraredRemoterGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        battery    (int)        : Battery Level (1 ~ 4), 1 is empty and 4 is full.
        keys       (list[bool]) : 64 keys, true means this key is learned.
        version    (str)        : Firmware Version.
        tz         (int)        : Timezone of this device.
    """

    def __init__(self, data: dict):
        self.battery: int = data["battery"]
        self.keys: list[bool] = data["keys"]
        self.version: str = data["version"]
        self.tz: int = data["tz"]

class MultiOutletGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        state                (list[str]) : State of device's sockets, ["closed", "open"].
        delays_on            (int)       : The remain time of Delay ON; Unit of minute; 0 is OFF.
        delays_off           (int)       : The remain time of Delay OFF; Unit of minute; 0 is OFF.
        version              (str)       : Firmware Version of device.
        tz                   (int)       : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.state: list[str] = data["state"]
        self.delays_on: int = data["delays"][0]["on"]
        self.delays_off: int = data["delays"][0]["off"]
        self.version: str = data["version"]
        self.tz: int = data["tz"]
        
class LockGetStateData(BUDPResponse):
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
        
class OutletGetStateData(BUDPResponse):
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
        
class SpeakerHubGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        version                (str)  : Hub's Version.
        wifi_enable            (bool) : Is WiFi Connected.
        wifi_ssid              (str)  : Current connected Wi-Fi.
        wifi_ip                (str)  : Current IP of Wi-Fi.
        wifi_gateway           (str)  : Current Gateway of Wi-Fi.
        wifi_mask              (str)  : Current Subnet Mask of Wi-Fi.
        eth_enable             (bool) : Is Ethernet Connected.
        options_volume         (int)  : Global volume of device.
        options_enableBeep     (bool) : Is beep enabled. True means the device will make a beep when performing some actions, such as startup, modify settings.
        options_mute           (bool) : Is mute mode enabled. True means device will not make any sound, even if you receive a message.
    """

    def __init__(self, data: dict):
        self.version: str = data["version"]
        self.wifi_enable: bool = data["wifi"]["enable"]
        self.wifi_ssid: str = data["wifi"]["ssid"]
        self.wifi_ip: str = data["wifi"]["ip"]
        self.wifi_gateway: str = data["wifi"]["gateway"]
        self.wifi_mask: str = data["wifi"]["mask"]
        self.eth_enable: bool = data["eth"]["enable"]
        self.options_volume: int = data["options"]["volume"]
        self.options_enableBeep: bool = data["options"]["enableBeep"]
        self.options_mute: bool = data["options"]["mute"]
        
class ManipulatorGetStateData(BUDPResponse):
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
        
class VibrationSensorGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        online               (bool)  : Is device online.
        state                (str)   : State of this device, ["normal", "alert"].
        battery              (str)   : Level of device's battery, 0 to 4 means empty to full.
        alertInterval        (Optional[int]) : Interval of Continuous Alert.
        noVibrationDelay     (Optional[int]) : Time to enter No-Vibration state.
        version              (str)   : Firmware Version of device.
        reportAt             (str)   : Time of reported.
        deviceId             (str)   : ID of device.
    """

    def __init__(self, data: dict):
        self.online: bool = data["state"]["online"]
        self.state: str = data["state"]["state"]
        self.battery: str = data["state"]["battery"]
        self.alertInterval: int | None = data["state"].get("alertInterval")
        self.noVibrationDelay: int | None = data["state"].get("noVibrationDelay")
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"]
        
class MotionSensorGetStateData(BUDPResponse):
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
        
class SmartRemoterGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        event                (Optional[dict]) : The last reported event.
        event_keyMask        (int)            : Triggered keys of event. Bits 0-7 means keys 0-7.
        event_type           (str)            : The type of event, ["Press", "LongPress"].
        battery              (int)            : Level of device's battery, 0 to 4 means empty to full.
        version              (str)            : Firmware Version of device.
        reportAt             (str)            : Time of reported.
        deviceId             (str)            : ID of device.
    """

    def __init__(self, data: dict):
        self.event: dict | None = data["state"].get("event")
        self.event_keyMask: int = data["state"]["event"]["keyMask"] if self.event else None
        self.event_type: str = data["state"]["event"]["type"] if self.event else None
        self.battery: int = data["state"]["battery"]
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"]
        
class HubGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        version                (str)  : Hub's Version.
        wifi_enable            (bool) : Is WiFi Connected.
        wifi_ssid              (str)  : Current connected Wi-Fi.
        wifi_ip                (str)  : Current IP of Wi-Fi.
        wifi_gateway           (str)  : Current Gateway of Wi-Fi.
        wifi_mask              (str)  : Current Subnet Mask of Wi-Fi.
        eth_enable             (bool) : Is Ethernet Connected.
        eth_ip                 (str)  : Current IP of Ethernet.
        eth_gateway            (str)  : Current Gateway of Ethernet.
        eth_mask               (str)  : Current Subnet Mask of Ethernet.
    """

    def __init__(self, data: dict):
        self.version: str = data["version"]
        self.wifi_enable: bool = data["wifi"]["enable"]
        self.wifi_ssid: str = data["wifi"]["ssid"]
        self.wifi_ip: str = data["wifi"]["ip"]
        self.wifi_gateway: str = data["wifi"]["gateway"]
        self.wifi_mask: str = data["wifi"]["mask"]
        self.eth_enable: bool = data["eth"]["enable"]
        self.eth_ip: str = data["eth"]["ip"]
        self.eth_gateway: str = data["eth"]["gateway"]
        self.eth_mask: str = data["eth"]["mask"]
        
class LeakSensorGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        online               (bool)  : Is device online.
        state                (str)   : State of this device, ["normal", "alert"].
        battery              (str)   : Level of device's battery, 0 to 4 means empty to full.
        interval             (Optional[int]) : Interval of Continuous Alert.
        version              (str)   : Firmware Version of device.
        reportAt             (str)   : Time of reported.
        deviceId             (str)   : ID of device.
    """

    def __init__(self, data: dict):
        self.online: bool = data["state"]["online"]
        self.state: str = data["state"]["state"]
        self.battery: str = data["state"]["battery"]
        self.interval: int | None = data["state"].get("interval")
        self.version: str = data["state"]["version"]
        self.reportAt: str = data["reportAt"]
        self.deviceId: str = data["deviceId"]
        
class SwitchGetStateData(BUDPResponse):
    """
    Represents the data of a BUDP data packet for the YoLink API.

    Attributes:
        state                (str)  : State of device, ["closed", "open"].
        delay_on             (int)  : The remain time of Delay ON; Unit of minute; 0 is OFF.
        delay_off            (int)  : The remain time of Delay OFF; Unit of minute; 0 is OFF.
        version              (str)  : Firmware Version of device.
        tz                   (int)  : Timezone of device. -12 ~ 12.
    """

    def __init__(self, data: dict):
        self.state: str = data["state"]
        self.delay_on: int = data["delay"]["on"]
        self.delay_off: int = data["delay"]["off"]
        self.version: str = data["version"]
        self.tz: int = data["tz"]
        
class LockGetStateData(BUDPResponse):
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