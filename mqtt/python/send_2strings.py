"""

DeviceHUB.net sample code for sending 2 strings.

In this example the strings are simulated.

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
STRING_NAME1    = 'paste_your_first_STRING_NAME_here'
STRING_NAME2    = 'paste_your_second_STRING_NAME_here'

# simulation for sensors
data1 = "StringTest1"
data2 = "StringTest2"

def string(id, device, sensor):
    global data1
    global data2
    
    if id == '1':
        print "String1: ", data1
        sensor.addValue(data1)
        device.send()
    else:   
        print "String2: ", data2
        sensor.addValue(data2)
        device.send()

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

STR1 = Sensor(Sensor.STRING, STRING_NAME1)
STR2 = Sensor(Sensor.STRING, STRING_NAME2)

device.addSensor(STR1)
device.addSensor(STR2)

threads = []

while True:
    t1 = threading.Thread(target=string, args=('1', device, STR1))
    t2 = threading.Thread(target=string, args=('2', device, STR2))
    threads.append(t1)
    threads.append(t2)
    t1.start()
    sleep(0.1)
    t2.start()
    sleep(5.0)