# Import RPi libraries
import RPi.GPIO as GPIO # For PWM
import time
from gpiozero import AngularServo # For direct commands to servo

servo = AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def set_angle(angle):
    servo.angle = angle
    time.sleep(1)

try:
    while True:
        set_angle(60)

except KeyboardInterrupt:
    print("Program exiting...")