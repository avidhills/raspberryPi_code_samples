"""

DeviceHUB.net sample code for sending a digital sensor and a analog sensor.

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
AN_SENSOR_NAME  = 'paste_your_analog_SENSOR_NAME_here'
DI_SENSOR_NAME  = 'paste_your_digital_SENSOR_NAME_here'

# simulation for sensors
InputDigital = 0
InputAnalog = 42

def gpio_input(gpio_input, device, sensor):
    global InputDigital
    global InputAnalog
    
    sensor.addValue(gpio_input)
    device.send()
    print gpio_input
    return

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

DI1 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME)
AN1 = Sensor(Sensor.ANALOG, AN_SENSOR_NAME)

device.addSensor(DI1)
device.addSensor(AN1)

threads = []

while True:
    t1 = threading.Thread(target=gpio_input, args=(InputDigital, device, DI1))
    t2 = threading.Thread(target=gpio_input, args=(InputAnalog, device, AN1))
    threads.append(t1)
    threads.append(t2)
    t1.start()
    sleep(0.1)
    t2.start()
    sleep(5.0)