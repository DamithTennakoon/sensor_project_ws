import time
import board
import busio
import adafruit_tsl2591
import pyodbc
import random
from datetime import datetime
import time

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the TSL2591 sensor
sensor = adafruit_tsl2591.TSL2591(i2c)

# Define the connection parameters for the remote Linux machine
server = '130.63.226.12'  # Replace with the IP address of your remote Linux machine
database = 'sensorDatabase'  # Replace with the name of your database
username = 'SA'  # Replace with your SQL Server username
password = 'Secretpassword123'  # Replace with your SQL Server password

# Create a connection string for the remote SQL Server
con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                     f'Server={server};'
                     f'Database={database};'
                     f'UID={username};'
                     f'PWD={password};')

# Create SQL cursor using connection object
cursor = con.cursor()

# Loop to continuously insert data
try:
    while True:
        # Generate random values for temperature and light  (SIMUALTED)
        test_temperature = round(random.uniform(15.0, 30.0), 2)  # Random temperature between 15.0 and 30.0
        # Read the brightness (lux) from the sensor (REAL)
        lux = float(sensor.lux)

        # Define test data
        test_time = datetime.now()  # Current timestamp
        test_id = 'rpi_1'

        # Insert data into the Environment table
        insert_query = """
        INSERT INTO Environment (Time, Id, Temperature, Light)
        VALUES (?, ?, ?, ?)
        """
        
        cursor.execute(insert_query, (test_time, test_id, test_temperature, lux))
        con.commit()
        
        # Print confirmation
        print(f"Data inserted: Time={test_time}, Id={test_id}, Temperature={test_temperature}, Light={lux}")
        
        # Wait for 10 seconds before inserting the next record
        time.sleep(1)

except pyodbc.Error as e:
    print("Error inserting data:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    con.close()