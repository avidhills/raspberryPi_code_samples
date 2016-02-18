
from devicehub import Sensor, Actuator, Device, Project
import threading
from Adafruit_PWM_Servo_Driver import PWM
import time

PROJECT_ID     = 'paste_your_PROJECT_ID_here'
DEVICE_UUID    = 'paste_your_DEVICE_UUID_here'
API_KEY        = 'paste_your_API_KEY_here'

ACTUATOR_NAME1 = 'ACTUATOR_DI1'


# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 350  # Min pulse length out of 4096
servoMax = 550  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

# Effect of actuator here

def switchRelay(ID, state):
    if ID == '1': 
        if state == '1':  
            pwm.setPWM(0, 0, servoMin)
            time.sleep(0.1)
            pwm.setPWM(1, 0, servoMin)
            time.sleep(0.1)
            pwm.setPWM(2, 0, servoMin)
            time.sleep(0.1)
            pwm.setPWM(3, 0, servoMin)
            

        else:
            pwm.setPWM(0, 0, servoMax)
            time.sleep(0.1)
            pwm.setPWM(1, 0, servoMax)
            time.sleep(0.1)
            pwm.setPWM(2, 0, servoMax)
            time.sleep(0.1)
            pwm.setPWM(3, 0, servoMax)
           

    print "servo ", "state: ", state
    
def act1_callback(payload):
    """
    :param payload: mqtt payload message
    """

    switchRelay('1', ACT1.state)



project = Project(PROJECT_ID)
device  = Device(project, DEVICE_UUID, API_KEY)


ACT1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME1)

device.addActuator(ACT1, act1_callback)

threads = []

while True:
    time.sleep(5.0)
