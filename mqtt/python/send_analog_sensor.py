"""

DeviceHUB.net sample code for sending an analog sensor.

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
AN_SENSOR_NAME  = 'paste_your_analog_SENSOR_NAME_here'

# simulation for sensor
InputAnalog = 42

def gpio_input(gpio_input, device, sensor):
    global InputAnalog
     
    sensor.addValue(gpio_input)
    device.send()
    print gpio_input
    return

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

AN1 = Sensor(Sensor.ANALOG, AN_SENSOR_NAME)

device.addSensor(AN1)

threads = []

while True:
    t1 = threading.Thread(target=gpio_input, args=(InputAnalog, device, AN1))
    threads.append(t1)
    t1.start()
    sleep(5.0)