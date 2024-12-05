# Import RPi libraries
import RPi.GPIO as GPIO
import time 

# Board setup
servoGpioPin = 18
GPIO.setmode(GPIO.BCM) # BCM: Broadcom SOC channel
GPIO.setup(servoGpioPin, GPIO.OUT)

pin = GPIO.PWM(servoGpioPin, 50) # Set GPIO pin 17 to operate at 50Hz 
pin.start(0) # Duty cycle for MG996R servo - units ms
try:
    while True:
        pin.ChangeDutyCycle(7.5) # 0
        time.sleep(2)
        
except KeyboardInterrupt:
    pin.stop()
    GPIO.cleanup()