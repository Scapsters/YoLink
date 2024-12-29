from collections import OrderedDict
from typing import Dict, Type
from Controller.YoLink_Controller import YoLinkController
from Api.DatabaseMySQL import DatabaseMySQL
from Interfaces.Device import Device
from Interfaces.Responses.Devices.Home import HomeGetDeviceListData
from Interfaces.Responses.Devices.THSensor import THSensorGetStateData
from Interfaces.Responses.Response import MethodNames
from Interfaces.Database import Database

# Yolink API Documentation: http://doc.yosmart.com/docs

# Approximation from https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html. "fairly accurate for relative humidity values above 50%"
GET_DEW_POINT = lambda temperature, humidity: temperature - ((100 - humidity )/5)
USE_FAHRENHEIT = True
CONVERT_TEMP = lambda temp: temp * 9/5 + 32 if USE_FAHRENHEIT else temp
SENSORS_WITH_DEWPOINT = {"THSensor"}
     
def main() -> None:
    
    # TODO: Im realizing the interfaces folder also has plenty of concrete classes. but theyre
    # pretty low level, and mostly dataclasses. thye can stay there probably...
    
    # TODO: file name consistency
    # TODO: Should main provide credentials? currently credentials are obtained in each class
    
    # Establish connection to MySQL Database
    database = DatabaseMySQL("scott")
    
    # Establish connection to YoLink API
    controller = YoLinkController()
    
    # Get connected devices
    devices_data: HomeGetDeviceListData = controller.make_request(
        MethodNames.HOME_GET_DEVICE_LIST, 
        HomeGetDeviceListData
    ).data
    devices: list[Device] = devices_data.devices
    
    # Create a list of every type of device
    device_types = set()
    for device in devices:
        device_types.add(device.type)
    
    # Create a dictionary in the format {deviceType: deviceInfo[]}
    devices_sorted = create_sorted_device_list(devices, device_types)
    
    for device_type in device_types:
        print_device_list(devices_sorted[device_type])
        print()
    
    poll_sensors(devices_sorted["THSensor"], controller, database)

def print_device_list(devices: list[Device]) -> None:
    '''
    Print the device list in a formatted table.
    
    Args:
        devices (list): A list of JSON BDUPs representing devices.
        
    Returns:    
        None
    '''
    column_titles = ["Type", "Name", "deviceID"]
    print("{: ^20} {: ^40} {: ^30}".format(*column_titles))

    for device in devices:
        device_information = [
            device.type, 
            device.name, 
            device.device_id
        ]
        print("{: <20} {: <40} {: <30}".format(*device_information))

# Given a list of json DBUPs representing devices and a set of each device type present, creates a list for each device type
def create_sorted_device_list(devices: list[Device], device_types: set[str]) -> Dict[str, list[Device]]:
    '''
    Create a dictionary in the format {deviceType: deviceInfo[]} from a list of devices.
    
    Args:
        devices (list): A list of JSON BDUPs representing devices.
        device_types (set): A set of strings representing the types of devices present.
        
    Returns:
        dict: A dictionary in the format {deviceType: deviceInfo[]}.
    '''
    
    devices_sorted_type: Dict[str, list[Device]] = {}
    
    # Create entries for each type
    for device_type in device_types:
        devices_sorted_type[device_type] = []
    
    # Populate entries
    for device in devices:
        devices_sorted_type[device.type].append(device)
    
    return devices_sorted_type

def poll_sensors(sensors: list[Device], controller: YoLinkController, database: Database):
    '''
    Not final.
    Poll the sensors and print the data. Only works for THSensors currently.
    TODO: Add support for other sensor types.
    '''
    
    # Print header for data
    column_titles = ["Sensor name", "Temp", "%Hum.", "Dew P"]
    print("{: ^35} {: ^6} {: ^6} {: ^6}".format(*column_titles))
        
    for sensor in sensors:
        sensor_data = controller.make_request(
            method_name = MethodNames.THSENSOR_GET_STATE, 
            device = sensor,
            response_type = THSensorGetStateData
        ).data
        
        # Access, process, and show data
        temperature = sensor_data.temperature
        humidity = sensor_data.humidity
        information = OrderedDict({ # Use an ordered dict to maintain order in csv file
            "name": sensor.name, 
            "temperature": round(CONVERT_TEMP(temperature), 1), 
            "humidity": humidity,
            "dew point": round(CONVERT_TEMP(GET_DEW_POINT(temperature, humidity)), 1)
        })
        print("{: <35} {: <6} {: <6} {: <6}".format(*information.values()))
        
        database.save("THSensor", information)

if __name__ == "__main__":
    main()