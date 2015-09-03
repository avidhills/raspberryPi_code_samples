"""

DeviceHUB.net sample code for getting 2 digital actuators state, and 
switch 2 relays, and sending analog and digital sensors.

In this example 2 relays are attached to GPIO 24 and GPIO 25 on Raspberry Pi,
and the 2 sensors are simulated.

First install Python API wrapper for devicehub.net
https://github.com/devicehubnet/devicehub_py

updated 02 September 2015
by Alexandru Gheorghe

"""

from devicehub import Sensor, Actuator, Device, Project
import threading
import RPi.GPIO as GPIO
from time import sleep

PROJECT_ID     = 'paste_your_PROJECT_ID_here'
DEVICE_UUID    = 'paste_your_DEVICE_UUID_here'
API_KEY        = 'paste_your_API_KEY_here'
DI_SENSOR_NAME = 'TEST_DI'
AN_SENSOR_NAME = 'TEST_AN'
ACTUATOR_NAME1 = 'ACTUATOR_DI1'
ACTUATOR_NAME2 = 'ACTUATOR_DI1'

# simulation for sensors
InputDigital = 0
InputAnalog = 42

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

def act2(client, userdata, message):
    """
    :param payload: mqtt payload message
    """

    switchRelay('2', ACT2.state)

def gpio_input(gpio_input, device, sensor):
 
    sensor.addValue(gpio_input)
    device.send()
    print gpio_input
    return

project = Project(PROJECT_ID)
device  = Device(project, DEVICE_UUID, API_KEY)

DI1  = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME)
AN1  = Sensor(Sensor.ANALOG, AN_SENSOR_NAME)
ACT1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME1)
ACT2 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME2)

device.addSensor(DI1)
device.addSensor(AN1)

device.addActuator(ACT1, act1_callback)
device.addActuator(ACT2, act2)

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