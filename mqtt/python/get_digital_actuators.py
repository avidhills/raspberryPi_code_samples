"""

DeviceHUB.net sample code for getting 2 digital actuators and switch 2 relays.

In this example 2 relays are attached to GPIO 24 and GPIO 25 on Raspberry Pi. 

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 02 September 2015
by Alexandru Gheorghe

"""



from devicehub import Sensor, Actuator, Device, Project
import RPi.GPIO as GPIO

PROJECT_ID     = 'paste_your_PROJECT_ID_here'
DEVICE_UUID    = 'paste_your_DEVICE_UUID_here'
API_KEY        = 'paste_your_API_KEY_here'
ACTUATOR_NAME1 = 'paste_your_first_ACTUATOR_NAME_here'
ACTUATOR_NAME2 = 'paste_your_second_ACTUATOR_NAME_here'


# init pins
GPIO_PIN1 = 24
GPIO_PIN2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN1, GPIO.OUT)
GPIO.setup(GPIO_PIN2, GPIO.OUT)
GPIO.output(GPIO_PIN1, False)
GPIO.output(GPIO_PIN2, False)

def switchRelay(ID, state):
    if ID == '1': 
        if state == '1':  
            GPIO.output(GPIO_PIN1, True)
        else:
            GPIO.output(GPIO_PIN1, False)
    if ID == '2':
        if state == '1':  
            GPIO.output(GPIO_PIN2, True)
        else:
            GPIO.output(GPIO_PIN2, False)

    print "PIN ", GPIO_PIN1, " state: ", state
    print "PIN ", GPIO_PIN2, " state: ", state
    
def act1_callback(payload):
    """
    :param payload: mqtt payload message
    """

    switchRelay('1', ACT1.state)

def act2_callback(payload):
    """
    :param payload: mqtt payload message
    """

    switchRelay('2', ACT2.state)


project = Project(PROJECT_ID)
device = Device(project, DEVICE_UUID, API_KEY)

ACT1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME1)
ACT2 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME2)

device.addActuator(ACT1, act1_callback)
device.addActuator(ACT2, act2_callback)

try:
    while True:
        pass
except KeyboardInterrupt:           
    GPIO.cleanup()