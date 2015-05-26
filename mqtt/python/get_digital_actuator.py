"""

DeviceHUB.net sample code for getting an digital actuator and switch a relay.

In this example a relay is attached to GPIO 24 on Raspberry Pi. 

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 26 May 2015
by Alexandru Gheorghe

"""


from devicehub import Sensor, Actuator, Device, Project
import threading
from time import sleep
import RPi.GPIO as GPIO
import json

PROJECT_ID     = 'paste_your_PROJECT_ID_here'
DEVICE_UUID    = 'paste_your_DEVICE_UUID_here'
API_KEY        = 'paste_your_API_KEY_here'
ACTUATOR_NAME1 = 'paste_your_ACTUATOR_NAME_here'


# init pin
GPIO_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, False)

def switchRelay(state):

    if state == 1:
        GPIO.output(GPIO_PIN, True)
    else:
        GPIO.output(GPIO_PIN, False)
    print "PIN ", GPIO_PIN, " state: ", state

    
def act1(client, userdata, message):
    """
    :param client:
    :param userdata:
    :param message:
    """
    # handles message arrived on subscribed topic
    msg = str(message.payload)
    j = json.loads(msg)
    act_state = j['state']
    print "act1", j['state']
    switchRelay(act_state)

project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

ACT1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME1)

device.addActuator(ACT1, act1)

try:
    while True:
        pass
except KeyboardInterrupt:           
    GPIO.cleanup()