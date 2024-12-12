import gpiod
import time

# GPIO setup
servo_gpio_pin = 18  # BCM pin number
chip = gpiod.Chip('gpiochip4')  # Replace 'gpiochip4' with the correct chip for your GPIO
line = chip.get_line(servo_gpio_pin)
line.request(consumer="Servo", type=gpiod.LINE_REQ_DIR_OUT)

# PWM parameters
frequency = 50  # 50Hz for standard servos
period = 1 / frequency  # Period in seconds
neutral_duty_cycle = 0.075  # Neutral position (1.5ms pulse width for 50Hz)

try:
    while True:
        # Generate a PWM pulse for neutral position
        line.set_value(1)  # High signal
        time.sleep(neutral_duty_cycle * period)
        line.set_value(0)  # Low signal
        time.sleep((1 - neutral_duty_cycle) * period)

        # Add delays to observe servo movement
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    line.release()
