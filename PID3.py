import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from matplotlib.animation import FuncAnimation

# Gaussian Noise Generator
class Gaussian:
    def __init__(self, mean=0, variance=1):
        self.mean = mean
        self.variance = variance

    def sample(self, size):
        return np.random.normal(self.mean, np.sqrt(self.variance), size)

# Initial conditions and PID parameters
initial_angle = 0
desired_angle = 90
time = np.linspace(0, 10, 1000)  # 1000 time points between 0 and 10 seconds
Kp = 1.0  # Proportional gain
Ki = 0.1  # Integral gain
Kd = 0.05  # Derivative gain

# PID controller transfer function
pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# System transfer function (integrator)
system = ctrl.TransferFunction([1], [1, 0])

# Combine PID and system in series (open-loop system)
open_loop_system = ctrl.series(pid, system)

# Create the closed-loop system with unity feedback
closed_loop_system = ctrl.feedback(open_loop_system, 1)

# Simulate system response to a step input (desired angle)
time, angle = ctrl.forced_response(closed_loop_system, time, desired_angle)

# Add Gaussian noise to the system's response
gauss = Gaussian(mean=0, variance=5)  # Noise with mean=0 and variance=5
noise = gauss.sample(angle.shape[0])  # Generate noise samples
angle_with_noise = angle + noise  # Add noise to the response

# Manual PID correction for noisy angle
corrected_angle = np.zeros_like(angle_with_noise)
for i in range(1, len(time)):
    error = desired_angle - angle_with_noise[i-1]
    corrected_angle[i] = (angle_with_noise[i-1] +
                          Kp * error +
                          Ki * np.sum(error) +
                          Kd * (error - (desired_angle - angle_with_noise[i-2])) if i > 1 else 0)

# Set up the figure and axis for real-time plotting
fig, ax = plt.subplots()
ax.set_title('Real-Time PID Control with Noise')
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
ax.yaxis.set_ticks(np.arange(0, 101, 10))
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (degrees)')
line1, = ax.plot([], [], label='Angle with Noise', color='red', linestyle='--')
line2, = ax.plot([], [], label='Corrected Angle', color='blue')
ax.legend()
ax.grid(True)

# Initialization function for the animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Update function for the animation
def update(frame):
    # Plot only up to the current frame (to simulate real-time)
    line1.set_data(time[:frame], angle_with_noise[:frame])
    line2.set_data(time[:frame], corrected_angle[:frame])
    return line1, line2

# Create animation object
ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=10)

# Show the plot with animation
plt.show()
