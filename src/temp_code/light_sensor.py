import time
import board
import busio
import adafruit_tsl2591

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the TSL2591 sensor
sensor = adafruit_tsl2591.TSL2591(i2c)

# Main loop to print brightness values in lux
while True:
    # Read the brightness (lux) from the sensor
    lux = sensor.lux

    # Check if lux value is valid (can be None if there's no valid reading)
    if lux is not None:
        #print(f"Brightness: {lux:.2f} lux")
        if (lux > 50.0):
            print("LIGHT ON")
        else:
            print("LIGHT OFF")
    else:
        print("Could not read lux value")

    # Wait for a bit before taking the next reading
    time.sleep(0.3)

