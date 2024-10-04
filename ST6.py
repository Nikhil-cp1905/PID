import time
import serial

class HW417:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=19200):
        self.ser = serial.Serial(port, baud_rate, timeout=1)
        print("HW-417 V1.2 initialized for USB communication on port:", port)

    def send_pwm_signal(self, channel, pwm_value):
        """Sends a PWM signal to the specified channel."""
        # Ensure channel is an integer and within the correct range
        channel = int(channel)
        pwm_value = int(pwm_value)

        # Create the command byte for PWM control
        # Assuming 0-255 for PWM values
        if channel == 1:
            command_byte = 0x01  # Command for motor 1
        elif channel == 2:
            command_byte = 0x02  # Command for motor 2
        else:
            raise ValueError("Invalid channel. Use 1 or 2.")

        # Create the message
        pwm_value_byte = pwm_value.to_bytes(1, byteorder='big')  # 1 byte for PWM value
        message = command_byte.to_bytes(1, byteorder='big') + pwm_value_byte

        # Send the PWM signal
        self.ser.write(message)

        # Print debug information
        print(f"Sent PWM Signal => Channel: {channel}, PWM Value: {pwm_value} => Bytes Sent: {list(message)}")
        time.sleep(0.5)  # Delay of 0.5 seconds

    def drive_motor1_forward(self, speed):
        self.send_pwm_signal(channel=1, pwm_value=speed)

    def drive_motor1_backward(self, speed):
        self.send_pwm_signal(channel=1, pwm_value=255 - speed)  # Reverse by inverting speed

    def drive_motor2_forward(self, speed):
        self.send_pwm_signal(channel=2, pwm_value=speed)

    def drive_motor2_backward(self, speed):
        self.send_pwm_signal(channel=2, pwm_value=255 - speed)  # Reverse by inverting speed

    def stop_motor1(self):
        self.send_pwm_signal(channel=1, pwm_value=0)

    def stop_motor2(self):
        self.send_pwm_signal(channel=2, pwm_value=0)

    def close(self):
        """Close the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    hw417 = HW417(port='/dev/ttyUSB0', baud_rate=19200)

    # Drive motor 1 forward at full speed
    hw417.drive_motor1_forward(255)

    # Drive motor 1 backward at half speed
    hw417.drive_motor1_backward(128)

    # Drive motor 2 forward at full speed
    hw417.drive_motor2_forward(255)

    # Stop motor 1
    hw417.stop_motor1()

    # Stop motor 2
    hw417.stop_motor2()

    # Close the serial connection
    hw417.close()

