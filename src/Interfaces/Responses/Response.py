from enum import Enum
from typing import Any, Tuple, Type, TypeVar, Generic
from pydantic.dataclasses import dataclass
from pydantic import BaseModel

T = TypeVar('T', bound='ResponseData')

class Response(Generic[T]):
    """
    Class to represent common data between Responses. Specifics lie within the data.
    """

    def __init__(self, response_json: dict, response_type: Type[T]):
        self.time   = response_json["time"]
        self.method = response_json["method"]
        self.msgid  = response_json["msgid"]
        self.code   = response_json["code"]
        self.desc   = response_json.get("desc")
        
        response_data = response_json.get("data")
        if response_data is not None:
            self.data: T = response_type(response_data)

@dataclass
class ResponseData():
    '''
    Abstract base class for ResponseData
    '''
    
    def __init__(self, data: dict):
        raise NotImplementedError
    
    def print_data(self):
        self.print_data_header()
        for row in self.data:
            self.print_data_row(row)
    
    def print_data_header(self):
        raise NotImplementedError()
    
    def print_data_row(self, row: Tuple[str, Any]):
        raise NotImplementedError()
    
from Interfaces.Responses.Devices.DoorSensor import DoorSensorGetStateData
from Interfaces.Responses.Devices.THSensor import THSensorGetStateData
from Interfaces.Responses.Devices.WaterMeterController import WaterMeterControllerGetStateData
from Interfaces.Responses.Devices.InfraredRemoter import InfraredRemoterGetStateData
from Interfaces.Responses.Devices.MultiOutlet import MultiOutletGetStateData
from Interfaces.Responses.Devices.Lock import LockGetStateData
from Interfaces.Responses.Devices.Outlet import OutletGetStateData
from Interfaces.Responses.Devices.SpeakerHub import SpeakerHubGetStateData
from Interfaces.Responses.Devices.Manipulator import ManipulatorGetStateData
from Interfaces.Responses.Devices.VibrationSensor import VibrationSensorGetStateData
from Interfaces.Responses.Devices.MotionSensor import MotionSensorGetStateData
from Interfaces.Responses.Devices.SmartRemoter import SmartRemoterGetStateData
from Interfaces.Responses.Devices.Hub import HubGetStateData
from Interfaces.Responses.Devices.LeakSensor import LeakSensorGetStateData
from Interfaces.Responses.Devices.Switch import SwitchGetStateData
from Interfaces.Responses.Devices.Home import HomeGetDeviceListData

class MethodNames(Enum):
    THSENSOR_GET_STATE = "THSensor.getState"
    WATERMETERCONTROLLER_GET_STATE = "WaterMeterController.getState"
    DOORSENSOR_GET_STATE = "DoorSensor.getState"
    INFRAREDREMOTER_GET_STATE = "InfraredRemoter.getState"
    MULTIOUTLET_GET_STATE = "MultiOutlet.getState"
    LOCK_GET_STATE = "Lock.getState"
    OUTLET_GET_STATE = "Outlet.getState"
    SPEAKERHUB_GET_STATE = "SpeakerHub.getState"
    MANIPULATOR_GET_STATE = "Manipulator.getState"
    VIBRATIONSENSOR_GET_STATE = "VibrationSensor.getState"
    MOTIONSENSOR_GET_STATE = "MotionSensor.getState"
    SMARTREMOTER_GET_STATE = "SmartRemoter.getState"
    HUB_GET_STATE = "Hub.getState"
    LEAKSENSOR_GET_STATE = "LeakSensor.getState"
    SWITCH_GET_STATE = "Switch.getState"
    HOME_GET_DEVICE_LIST = "Home.getDeviceList"

def get_response_type(sensor_type: str, method: MethodNames) -> type:
    """
    Factory method to create a BUDPResponse object based on the sensor type and method.

    Args:
    sensor_type (str): The type of sensor.
    method (str): The method used to get the data.
    data (dict): The data to be used to create the response.

    Returns:
    BUDPResponse: The response object.
    """
    response_classes: dict[tuple[str, MethodNames], type] = {
        ("THSensor", MethodNames.THSENSOR_GET_STATE): THSensorGetStateData,
        ("WaterMeterController", MethodNames.WATERMETERCONTROLLER_GET_STATE): WaterMeterControllerGetStateData,
        ("DoorSensor", MethodNames.DOORSENSOR_GET_STATE): DoorSensorGetStateData,
        ("InfraredRemoter", MethodNames.INFRAREDREMOTER_GET_STATE): InfraredRemoterGetStateData,
        ("MultiOutlet", MethodNames.MULTIOUTLET_GET_STATE): MultiOutletGetStateData,
        ("Lock", MethodNames.LOCK_GET_STATE): LockGetStateData,
        ("Outlet", MethodNames.OUTLET_GET_STATE): OutletGetStateData,
        ("SpeakerHub", MethodNames.SPEAKERHUB_GET_STATE): SpeakerHubGetStateData,
        ("Manipulator", MethodNames.MANIPULATOR_GET_STATE): ManipulatorGetStateData,
        ("VibrationSensor", MethodNames.VIBRATIONSENSOR_GET_STATE): VibrationSensorGetStateData,
        ("MotionSensor", MethodNames.MOTIONSENSOR_GET_STATE): MotionSensorGetStateData,
        ("SmartRemoter", MethodNames.SMARTREMOTER_GET_STATE): SmartRemoterGetStateData,
        ("Hub", MethodNames.HUB_GET_STATE): HubGetStateData,
        ("LeakSensor", MethodNames.LEAKSENSOR_GET_STATE): LeakSensorGetStateData,
        ("Switch", MethodNames.SWITCH_GET_STATE): SwitchGetStateData,
        ("No Device", MethodNames.HOME_GET_DEVICE_LIST): HomeGetDeviceListData,
    }

    return response_classes[(sensor_type, method)]