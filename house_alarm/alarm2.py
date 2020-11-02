import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

AlarmPin = 24
SensorPin = 4
pwmChannel = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(SensorPin, GPIO.IN)
GPIO.setup(AlarmPin, GPIO.OUT)
GPIO.setup(pwmChannel, GPIO.OUT)
GPIO.output(AlarmPin, GPIO.HIGH)
pwm = GPIO.PWM(pwmChannel, 1000)
GPIO.SetPWMrange(pwmChannel, 5000)

def Beep(x):
    GPIO.output(AlarmPin, GPIO.LOW)
    time.sleep(x)
    GPIO.output(AlarmPin, GPIO.HIGH)
    time.sleep(x)
    
def dontBeep():
    GPIO.output(AlarmPin, GPIO.LOW)

try:
    while True:
        if (GPIO.input(SensorPin) == True):
            print("I SEE SOMETHING")
            #Beep(0.0001)
            pwm.start(20)
            
        else:
            #dontBeep()
            print("ITS SAFE NOW")
            pwm.stop()
            
except KeyboardInterrupt:
    print("ctl+c Stopping")
    
pwm.stop()
GPIO.cleanup()
        