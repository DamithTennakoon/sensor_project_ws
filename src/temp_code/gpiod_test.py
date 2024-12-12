import gpiod
import time

# Define the GPIO pin and chip
LED_PIN = 18  # Change to your desired pin number
chip = gpiod.Chip('gpiochip4')  # Chip managing the pin

# Get the GPIO line and set it as output
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        # Turn LED on
        led_line.set_value(1)
        time.sleep(1)
        # Turn LED off
        led_line.set_value(0)
        time.sleep(1)
finally:
    led_line.release()
