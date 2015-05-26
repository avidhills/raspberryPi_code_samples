"""

DeviceHUB.net sample code for sending a digital sensor.

In this example the sensor is simulated.

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
DI_SENSOR_NAME  = 'paste_your_digital_SENSOR_NAME_here'

# simulation for sensors
InputDigital = 0

def gpio_input(gpio_input, device, sensor):
    global InputDigital
    
    sensor.addValue(gpio_input)
    device.send()
    print gpio_input
    return

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

DI1 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME)

device.addSensor(DI1)

threads = []

while True:
    t1 = threading.Thread(target=gpio_input, args=(InputDigital, device, DI1))
    threads.append(t1)
    t1.start()
    sleep(5.0)