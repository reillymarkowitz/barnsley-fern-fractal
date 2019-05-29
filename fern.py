#!/usr/bin/env Python3

'''
Barnsley Fern fractal
Reilly Markowitz
5/29/19
'''

import random
import numpy as np
import matplotlib.pyplot as plt

# List of vectors in R2,
# starting at the origin
points = [np.array([0, 0])]

for i in range(100000):
    rand = random.randrange(100)

    # ~1% chance
    if rand < 1:
        vector = np.array([0, 0])

        matrix = np.array(  [[0.00, 0.00],
                             [0.00, 0.16]] )
    # ~85% chance
    elif rand < 86:
        vector = np.array([0, 1.6])

        matrix = np.array(  [[ 0.85, 0.04],  
                             [-0.04, 0.85]] )
    # ~7% chance
    elif rand < 93:
        vector = np.array([0, 1.6])

        matrix = np.array(  [[0.20, -0.26],
                             [0.23,  0.22]] )
    # ~7% chance
    else:
        vector = np.array([0, 0.44])

        matrix = np.array(  [[-0.15, 0.28],
                             [ 0.26, 0.24]] )

    # Add the vector to the dot product
    # of the matrix and the last point
    # to get the next point
    nextPoint = np.dot(matrix, points[-1]) + vector
    points.append(nextPoint)

# Split the points into lists of
# x-coordinates and y-coordinates
x_coords, y_coords = zip(*points)

# Plot the points
plt.scatter(x_coords, y_coords, s=0.5, color='g')
plt.gcf().canvas.set_window_title('Barnsley Fern Fractal')
plt.show()
