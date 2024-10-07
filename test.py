import serial
import time

# Open the serial port (change '/dev/ttyUSB0' to your actual port)
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.timeout = 1

try:
    while True:
        # Motor 1: Move forward
        motor1_forward_speed = 60  # Speed from 1 to 127
        motor1_forward_byte = bytes([motor1_forward_speed])
        print(f"Motor 1 - Sending forward speed: {motor1_forward_speed} (byte value: {motor1_forward_byte})")
        ser.write(motor1_forward_byte)  # Send as byte
        time.sleep(2)

        # Motor 2: Move forward
        motor2_forward_speed = 70  # Speed from 1 to 127
        motor2_forward_byte = bytes([motor2_forward_speed + 4])  # Add 4 for motor 2 command offset
        print(f"Motor 2 - Sending forward speed: {motor2_forward_speed} (byte value: {motor2_forward_byte})")
        ser.write(motor2_forward_byte)  # Send as byte
        time.sleep(2)

        # Stop both motors
        stop_byte = bytes([0])
        print(f"Motor 1 - Sending stop command (byte value: {stop_byte})")
        ser.write(stop_byte)  # Stop Motor 1
        print(f"Motor 2 - Sending stop command (byte value: {stop_byte})")
        ser.write(stop_byte)  # Stop Motor 2
        time.sleep(2)

        # Motor 1: Move backward
        motor1_backward_speed = 60  # Speed from 1 to 127
        motor1_backward_byte = bytes([motor1_backward_speed + 128])  # Add 128 for backward
        print(f"Motor 1 - Sending backward speed: {motor1_backward_speed + 128} (byte value: {motor1_backward_byte})")
        ser.write(motor1_backward_byte)  # Send as byte
        time.sleep(2)

        # Motor 2: Move backward
        motor2_backward_speed = 70  # Speed from 1 to 127
        motor2_backward_byte = bytes([motor2_backward_speed + 128 + 4])  # Add 128 for backward, 4 for motor 2
        print(f"Motor 2 - Sending backward speed: {motor2_backward_speed + 128} (byte value: {motor2_backward_byte})")
        ser.write(motor2_backward_byte)  # Send as byte
        time.sleep(2)

        # Stop both motors
        print(f"Motor 1 - Sending stop command (byte value: {stop_byte})")
        ser.write(stop_byte)  # Stop Motor 1
        print(f"Motor 2 - Sending stop command (byte value: {stop_byte})")
        ser.write(stop_byte)  # Stop Motor 2
        time.sleep(2)

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    ser.close()  # Close the serial port when done
