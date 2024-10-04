import time

class SabertoothController:
    def __init__(self):
        """Initialize the Sabertooth controller (simulated)."""
        self.motor_state = "stopped"  # Initial state of the motor
        self.speed = 0  # Speed level of the motor

    def send_command(self, command):
        """Simulate sending a command to the Sabertooth."""
        if command == 0:
            self.stop_motor()
        elif 128 <= command <= 255:
            self.move_forward(command)
        elif 1 <= command <= 127:
            self.move_backward(command)
        else:
            print(f"Invalid command: {command}")

    def move_forward(self, speed):
        """Simulate moving the motor forward at a given speed (128-255)."""
        self.motor_state = "moving forward"
        self.speed = speed
        print(f"Motor state: {self.motor_state} at speed: {self.speed}")

    def move_backward(self, speed):
        """Simulate moving the motor backward at a given speed (1-127)."""
        self.motor_state = "moving backward"
        self.speed = speed
        print(f"Motor state: {self.motor_state} at speed: {self.speed}")

    def stop_motor(self):
        """Simulate stopping the motor."""
        self.motor_state = "stopped"
        self.speed = 0
        print("Motor state: stopped")

def simulate_sabertooth_operation():
    """Simulate the operation of the Sabertooth motor controller."""
    sabertooth = SabertoothController()

    try:
        while True:
            # Simulate forward movement
            print("\nSimulating motor moving forward...")
            sabertooth.send_command(200)  # Speed value for forward movement
            time.sleep(2)  # Run forward for 2 seconds

            # Simulate stopping the motor
            print("Stopping motor...")
            sabertooth.send_command(0)  # Command to stop the motor
            time.sleep(1)  # Pause before reversing

            # Simulate backward movement
            print("\nSimulating motor moving backward...")
            sabertooth.send_command(50)  # Speed value for backward movement
            time.sleep(2)  # Run backward for 2 seconds

            # Simulate stopping the motor
            print("Stopping motor...")
            sabertooth.send_command(0)  # Command to stop the motor
            time.sleep(2)  # Delay before the next cycle

    except KeyboardInterrupt:
        print("Simulation interrupted.")

if __name__ == "__main__":
    simulate_sabertooth_operation()

