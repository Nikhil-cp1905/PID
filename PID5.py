import numpy as np
import matplotlib.pyplot as plt
from simple_pid import PID
import random

# Motor parameters
desired_angle = 90  # Desired angle (degrees)
initial_angle = 0   # Initial angle (degrees)
time_steps = 100    # Number of time steps for simulation
dt = 0.1            # Time step duration (seconds)

# PID controller settings
pid = PID(1.2, 0.01, 0.05, setpoint=desired_angle)  # Kp, Ki, Kd values
pid.output_limits = (0, 90)  # Limit the PID output between 0 and 90

# Arrays to store the results
actual_angles = []
noisy_angles = []
corrected_angles = []

# Simulate the motor angle over time
angle = initial_angle
for i in range(time_steps):
    # Add noise to the angle (random noise between -5 and 5 degrees)
    noise = random.uniform(-5, 5)
    noisy_angle = angle + noise

    # Calculate the PID correction
    correction = pid(noisy_angle)

    # Apply the correction to the motor's angle (simulate motor response)
    angle = angle + correction * dt

    # Save the results
    actual_angles.append(angle)
    noisy_angles.append(noisy_angle)
    corrected_angles.append(correction)

# Time array for plotting
time = np.linspace(0, time_steps*dt, time_steps)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(time, noisy_angles, label="Noisy Angle", color="r", linestyle="--")
plt.plot(time, actual_angles, label="Corrected Angle", color="b")
plt.axhline(y=desired_angle, color='g', linestyle='-', label="Desired Angle")
plt.title("Motor Angle with PID Correction and Noise")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.legend()
plt.grid(True)
plt.show()
