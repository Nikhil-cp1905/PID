import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define points for each letter in the word "AYUS"
# A simplified representation of each letter using line segments
points = {
    'A': [(0, 0), (0.5, 1), (1, 0), (0.25, 0.5), (0.75, 0.5)],
    'Y': [(1.5, 1), (2, 0.5), (2.5, 1), (2, 0.5), (2, 0)],
    'U': [(3, 1), (3, 0), (4, 0), (4, 1)],
    'S': [(4.5, 1), (5, 1), (4.5, 0.5), (4.5, 0), (5, 0)]
}

# Flatten the points into a continuous list for easy animation
x_points = []
y_points = []
for letter in "AYUS":
    for point in points[letter]:
        x_points.append(point[0])
        y_points.append(point[1])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(-0.5, 1.5)

# Initialize an empty line
line, = ax.plot([], [], lw=2)

# Function to initialize the animation
def init():
    line.set_data([], [])
    return line,

# Function to update the line for each frame
def update(frame):
    # Update the line to show the current segment of the points
    line.set_data(x_points[:frame], y_points[:frame])
    return line,

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=len(x_points), init_func=init, blit=True, interval=100)

# Display the animation
plt.show()
