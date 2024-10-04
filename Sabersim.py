import time

class VirtualSabertoothController:
    def __init__(self):
        # Initial state of the virtual motor
        self.state = "stopped"
        self.speed = 0

    def send_command(self, command):
        """Simulate sending a command to Sabertooth."""
        print(f"Sending command: {command} (speed: {self.speed})")
        time.sleep(0.1)  # Simulate processing delay

    def move_motor(self, speed):
        """
        Simulate controlling the motor speed.
        Speed values:
        - 0 to 127: Reverse
        - 128 to 255: Forward
        """
        if 0 <= speed <= 255:
            self.speed = speed
            if speed == 0:
                self.state = "stopped"
            elif 1 <= speed <= 127:
                self.state = "moving backward"
            elif 128 <= speed <= 255:
                self.state = "moving forward"

            self.send_command(self.speed)
            print(f"Motor state: {self.state}, Speed: {self.speed}")
        else:
            print("Invalid speed. Speed value must be between 0 and 255.")

    def stop_motor(self):
        """Simulate stopping the motor."""
        print("Stopping motor...")
        self.move_motor(0)

def simulate_sabertooth_operation():
    # Create a virtual Sabertooth controller
    sabertooth = VirtualSabertoothController()

    # Simulate forward movement
    print("\nSimulating motor moving forward...")
    sabertooth.move_motor(200)  # Simulate moving forward with a speed of 200
    time.sleep(2)  # Simulate motor running for 2 seconds

    # Simulate stopping the motor
    sabertooth.stop_motor()
    time.sleep(1)  # Pause before reversing

    # Simulate backward movement
    print("\nSimulating motor moving backward...")
    sabertooth.move_motor(50)  # Simulate moving backward with a speed of 50
    time.sleep(2)  # Simulate motor running for 2 seconds

    # Simulate stopping the motor
    sabertooth.stop_motor()

if __name__ == "__main__":
    simulate_sabertooth_operation()
