import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the cube
vertices = np.array([
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1]
])

# Define the faces of the cube
faces = [
    [0, 1, 2, 3],
    [0, 3, 7, 4],
    [1, 5, 6, 2],
    [5, 4, 7, 6],
    [0, 4, 5, 1],
    [3, 2, 6, 7]
]

# Create a figure and axes
fig, ax = plt.subplots()
ax = fig.gca()

# Set the axes limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Draw the cube
ax.plot(vertices[:, 0], vertices[:, 1], vertices[:, 2], 'b-')

# Rotate the cube
for angle in range(360):
    vertices = np.dot(vertices, np.array([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ]))

    ax.clear()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.plot(vertices[:, 0], vertices[:, 1], vertices[:, 2], 'b-')

#
print(hasattr(ax, 'set_zlim'))
