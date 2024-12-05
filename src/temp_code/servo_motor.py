import gpiod
import time

# Constants
CHIP = "gpiochip0"  # Default GPIO chip
LINE_OFFSET = 18    # BCM pin 18
PWM_FREQUENCY = 50  # Frequency in Hz (standard for servo motors)
DUTY_NEUTRAL = 7.5  # Neutral position duty cycle (in %)

# Calculate the period and pulse width
PERIOD_NS = int(1_000_000_000 / PWM_FREQUENCY)  # Period in nanoseconds
DUTY_NS = int((DUTY_NEUTRAL / 100) * PERIOD_NS) # Neutral position in nanoseconds

# Setup GPIO
chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE_OFFSET)

config = gpiod.LineRequest()
config.consumer = "servo_control"
config.request_type = gpiod.LINE_REQUEST_DIRECTION_OUTPUT

line.request(config)

try:
    # Generate PWM manually
    while True:
        # High phase
        line.set_value(1)
        time.sleep(DUTY_NS / 1_000_000_000)  # Convert ns to seconds
        
        # Low phase
        line.set_value(0)
        time.sleep((PERIOD_NS - DUTY_NS) / 1_000_000_000)

except KeyboardInterrupt:
    # Cleanup
    line.set_value(0)
    line.release()
    chip.close()
