import pymssql
import random
from datetime import datetime
import time
import board
import busio
import adafruit_tsl2591

# Define the connection parameters for the remote SQL Server
server = '130.63.226.12'  # Replace with the IP address of your remote SQL Server
database = 'sensorDatabase'  # Replace with the name of your database
username = 'SA'  # Replace with your SQL Server username
password = 'Secretpassword123'  # Replace with your SQL Server password

# Create a connection to the remote SQL Server using pymssql
con = pymssql.connect(
    server=server,
    user=username,
    password=password,
    database=database
)

# Create SQL cursor using connection object
cursor = con.cursor()

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the TSL2591 sensor
sensor = adafruit_tsl2591.TSL2591(i2c)

# Loop to continuously insert data
try:
    while True:
        # Generate random values for temperature and light
        test_temperature = round(random.uniform(15.0, 30.0), 2)  # Random temperature between 15.0 and 30.0
        lux = sensor.lux
        lux = round(lux, 2)
        
        # Define test data
        test_time = datetime.now()  # Current timestamp
        test_id = 'rpi_1'
        
        # Insert data into the Environment table
        insert_query = """
        INSERT INTO Environment (Time, Id, Temperature, Light)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(insert_query, (test_time, test_id, test_temperature, lux))
        con.commit()
        
        # Print confirmation
        print(f"Data inserted: Time={test_time}, Id={test_id}, Temperature={test_temperature}, Light={lux}")
        
        # Wait for 1 second before inserting the next record
        time.sleep(1)

except pymssql.Error as e:
    print("Error inserting data:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    con.close()
