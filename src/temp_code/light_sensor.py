import pymssql
import random
from datetime import datetime
import time

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

# Loop to continuously insert data
try:
    while True:
        # Generate random values for temperature and light
        test_temperature = round(random.uniform(15.0, 30.0), 2)  # Random temperature between 15.0 and 30.0
        test_light = round(random.uniform(50.0, 100.0), 2)  # Random light level between 50.0 and 100.0
        
        # Define test data
        test_time = datetime.now()  # Current timestamp
        test_id = 'rpi_1'
        
        # Insert data into the Environment table
        insert_query = """
        INSERT INTO Environment (Time, Id, Temperature, Light)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(insert_query, (test_time, test_id, test_temperature, test_light))
        con.commit()
        
        # Print confirmation
        print(f"Data inserted: Time={test_time}, Id={test_id}, Temperature={test_temperature}, Light={test_light}")
        
        # Wait for 1 second before inserting the next record
        time.sleep(1)

except pymssql.Error as e:
    print("Error inserting data:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    con.close()
