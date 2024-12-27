from Interfaces.Responses.Response import ResponseData

class WaterMeterControllerGetStateData(ResponseData):
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
