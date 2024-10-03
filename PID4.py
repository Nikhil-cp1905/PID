import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

class Gaussian:
    def __init__(self, mean=0, variance=1):
        self.mean = mean
        self.variance = variance

    def sample(self, size):
        return np.random.normal(self.mean, np.sqrt(self.variance), size)

initial_angle = 0
desired_angle = 90
time = np.linspace(0, 50 , 1000)

# PID controller gains
Kp = 1.0
Ki = 0.1
Kd = 0.05

# PID transfer function
pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# System transfer function
system = ctrl.TransferFunction([1], [1, 0])

# Open-loop and closed-loop system
open_loop_system = ctrl.series(pid, system)
closed_loop_system = ctrl.feedback(open_loop_system, 1)

# Simulate system response
time, angle = ctrl.forced_response(closed_loop_system, time, desired_angle)

# Adding Gaussian noise
gauss = Gaussian(mean=0, variance=5)
noise = gauss.sample(angle.shape[0])
angle_with_noise = angle + noise

# PID correction loop
corrected_angle = np.zeros_like(angle_with_noise)
integral = 0
previous_error = 0

for i in range(1, len(time)):
    error = desired_angle - angle_with_noise[i-1]
    integral += error  # Accumulating the error for the integral term
    derivative = error - previous_error  # Derivative of the error
    previous_error = error  # Update previous error for the next iteration
    
    # PID correction formula
    corrected_angle[i] = (angle_with_noise[i-1] +
                          Kp * error +
                          Ki * integral +
                          Kd * derivative)

# Plotting the results
plt.figure()
plt.plot(time, angle_with_noise, label='Angle with Noise')
plt.plot(time, corrected_angle, label='Corrected Angle')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.title('PID Control of Angle with Noise Correction (Gaussian Noise)')
plt.grid(True)
plt.show()
