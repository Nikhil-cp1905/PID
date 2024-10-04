import time
class SabertoothSimulator:
    def __init__(self):
        """Initialize the Sabertooth simulator."""
        self.motor_state = "stopped"  # Initial state of the motor
        self.speed = 0  # Speed level of the motor

    def putc(self, data):
        """Simulate sending a byte to the Sabertooth."""
        print(f"Sending byte: {data}")

    def drive_forward(self, address, speed):
        """Simulate sending the DriveForward command."""
        if 0 <= address <= 127 and 0 <= speed <= 255:
            # Sending the command bytes
            self.putc(address)  # Send the address byte
            self.putc(0)       # Command byte for moving forward
            self.putc(speed)   # Speed byte
            checksum = (address + 0 + speed) & 0b01111111
            self.putc(checksum)  # Send checksum
            self.motor_state = "moving forward"
            self.speed = speed
            print(f"Motor state: {self.motor_state} at speed: {self.speed}")
        else:
            print("Invalid address or speed!")

    def stop_motor(self):
        """Simulate stopping the motor."""
        self.putc(0)  # Command to stop the motor
        self.motor_state = "stopped"
        self.speed = 0
        print("Motor state: stopped")

def simulate_motor_control():
    """Simulate the control of the Sabertooth motor controller."""
    simulator = SabertoothSimulator()
    
    try:
        # Simulate driving forward
        print("Simulating driving forward...")
        simulator.drive_forward(1, 200)  # Address 1, speed 200
        time.sleep(2)  # Simulate moving for 2 seconds

        # Simulate stopping the motor
        print("Stopping motor...")
        simulator.stop_motor()
        time.sleep(1)  # Pause before reversing

        # Simulate driving backward (assuming similar function exists)
        print("Simulating driving backward...")
        simulator.drive_forward(1, 50)  # Address 1, speed 50 (reversed)
        time.sleep(2)  # Simulate moving for 2 seconds

        # Simulate stopping the motor again
        print("Stopping motor...")
        simulator.stop_motor()
        time.sleep(2)  # Delay before the next cycle

    except KeyboardInterrupt:
        print("Simulation interrupted.")

if __name__ == "__main__":
    simulate_motor_control()
