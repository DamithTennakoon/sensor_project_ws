# Import RPi libraries
import RPi.GPIO as GPIO # For PWM
import time
from gpiozero import AngularServo # For direct commands to servo
'''
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
    servo.angle = 90
    time.sleep(2)
    servo.angle = 0
    time.sleep(2)
    servo.angle = -90
    time.sleep(2)

'''
# Objective: control the servo motor over a udp server
import socket

# Function: decode the received msg into rpi value and move servo
# Q = +1 deg, W = -1 deg,...
def move_servo(msg):
    pass
    

# Construct main method
def main():
    # Define UDP server 
    host_ip = '130.63.230.54'
    port = 3232
    buffer_size = 1024
    client_ip = []
    msg_rx = ""
    msg_tx = "ISRU Rover Server"
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((host_ip, port))
    print("Server established - waiting client connection...")

    # Initialize servo motor
    target_servo_angle = 90
    servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
    time.sleep(1)
    servo.angle = target_servo_angle
    time.sleep(1)
    print("Servo motor initialized...")

    # Continous communication with clients
    while True:
        # Data reception and decoding
        msg_rx, client_ip = udp_server.recvfrom(buffer_size)
        msg_rx = msg_rx.decode('utf-8')
        print("RX: ", msg_rx)

        # Data encoding and transmission
        udp_server.sendto(msg_tx.encode('utf-8'), client_ip)

if __name__ == '__main__':
    main()








