import serial
import time
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) 
    print(f"Connected to {ser.portstr}") 
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")
    except Exception as e:
        print(f"Failed to send command: {e}")
send_command(64 + 43)  
send_command(192 + 43) 
time.sleep(2)  

send_command(64) 
send_command(192)  
time.sleep(1) 

send_command(64 - 43) 
send_command(192 - 43) 
time.sleep(2)

send_command(64)  
send_command(192) 


ser.close()
print("Serial connection closed.")

