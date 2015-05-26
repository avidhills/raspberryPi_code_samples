"""

DeviceHUB.net sample code for sending a string.

In this example the string is simulated.

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
STRING_NAME     = 'paste_your_STRING_NAME_here'

# simulation for string
data1 = "StringTest1"

def string(device, sensor):
    global data1

    print "String1:", data1
    sensor.addValue(data1)
    device.send()

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

STR1 = Sensor(Sensor.STRING, STRING_NAME)

device.addSensor(STR1)

threads = []

while True:
    t1 = threading.Thread(target=string, args=(device, STR1))
    threads.append(t1)
    t1.start()
    sleep(5.0)