"""

DeviceHUB.net sample code for sending 2 digital sensors.

In this example the sensors are simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 26 May 2015
by Alexandru Gheorghe

"""


from devicehub import Sensor, Actuator, Device, Project
import threading
from time import sleep

PROJECT_ID      = 'paste_your_PROJECT_ID_here'
DEVICE_UUID     = 'paste_your_DEVICE_UUID_here'
API_KEY         = 'paste_your_API_KEY_here'
DI_SENSOR_NAME1 = 'paste_your_first_digital_SENSOR_NAME_here'
DI_SENSOR_NAME2 = 'paste_your_second_digital_SENSOR_NAME_here'

# simulation for sensors
InputDigital1 = 0
InputDigital2 = 1

def gpio_input(id, device, sensor):
    global InputDigital1
    global InputDigital2
    
    if id == '1':
        sensor.addValue(InputDigital1)
        device.send()
        print InputDigital1
        return
    else: 
        sensor.addValue(InputDigital2)
        device.send()
        print InputDigital2
        return          

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

DI1 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME1)
DI2 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME2)

device.addSensor(DI1)
device.addSensor(DI2)

threads = []

while True:
    t1 = threading.Thread(target=gpio_input, args=('1', device, DI1))
    t2 = threading.Thread(target=gpio_input, args=('2', device, DI2))
    threads.append(t1)
    threads.append(t2)
    t1.start()
    sleep(0.1)
    t2.start()
    sleep(5.0)