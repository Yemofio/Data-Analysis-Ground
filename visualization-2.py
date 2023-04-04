import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add titles and labels
ax.set_title('Random Data Scatter Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Customize the axes
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_aspect('equal', adjustable='box')

# Add a colorbar
sc = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5)
cbar = fig.colorbar(sc)
cbar.set_label('Color Intensity')

# Save the plot to a file
fig.savefig('scatter_plot.png', dpi=300)

# Show the plot
plt.show()
