import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from gaussian import Gaussian  # Assuming you have the gaussian library installed

# Constants
initial_angle = 0
desired_angle = 90
time = np.linspace(0, 10, 1000)  # Time vector

# PID Controller parameters
Kp = 1.0
Ki = 0.1
Kd = 0.05

# PID Controller
pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# System to be controlled (simplified as an integrator)
system = ctrl.TransferFunction([1], [1, 0])

# Create the open-loop system (plant + controller)
open_loop_system = ctrl.series(pid, system)

# Create the closed-loop system with unity feedback
closed_loop_system = ctrl.feedback(open_loop_system, 1)

# Simulate the system response
time, angle = ctrl.forced_response(closed_loop_system, time, desired_angle)
mean=0
variance=5
# Add Gaussian noise using the gaussian library
gauss = Gaussian(mean,variance)
noise = gauss.sample(angle.shape[0])  # Assuming sample generates a list of noise values
angle_with_noise = angle + noise

# Apply the PID correction
corrected_angle = np.zeros_like(angle_with_noise)
for i in range(1, len(time)):
    error = desired_angle - angle_with_noise[i-1]
    corrected_angle[i] = angle_with_noise[i-1] + Kp * error + Ki * np.sum(error) + Kd * (error - (desired_angle - angle_with_noise[i-2])) if i > 1 else 0

# Plot results
plt.figure()
plt.plot(time, angle_with_noise, label='Angle with Noise')
plt.plot(time, corrected_angle, label='Corrected Angle')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.title('PID Control of Angle with Noise Correction (Gaussian Noise)')
plt.grid(True)
plt.show()
