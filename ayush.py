import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Set limits for the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initialize the text that we want to animate
text = ax.text(0, 5, 'Ayush', fontsize=30, ha='center', va='center')

# Function to update the animation frame
def update(frame):
    # Update the text's position
    text.set_x(frame)
    return text,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50, blit=True)

# Display the animation
plt.show()
