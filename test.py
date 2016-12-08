import time
from quickhull import *
from monotone import *
from chan import *
from grahm import *
from input_generator import *
# plotting
import matplotlib.pyplot as plt
import numpy as np

#rad = 10
#num_points = 100

#t = np.random.uniform(0.0, 2.0*np.pi, num_points)
#r = rad * np.sqrt(np.random.uniform(0.0, 1.0, num_points))
#x = r * np.cos(t)
#y = r * np.sin(t)

#print(x)
#print(y)

#plt.plot(x, y, "ro", ms=1)
#plt.axis([-15, 15, -15, 15])
#plt.show()

input_points_static = [ (1,1),
                        (2,2), (2,4),
                        (3,1), (3,4), (3,8),
                        (4,5),
                        (5,2),
                        (6,2), (6,7),
                        (7,5), 
                        (8,10)
                      ]

# Corner cases:
# All points on one side of dividing point
# 1 or 2 points total
# 1 point very far away from cluster
# close to a circular shape

num_points = 4000000

#input_points = input_points_static

# Random Distribution
input_points = generate_random_dist(num_points, 0, 10000)

# Skewed Random Distribution
#input_points = generate_skewed_dist(num_points, 0, 10000)

# Square Distribution
#input_points = generate_square_dist(num_points, 0, 10000)

# Circular Distribution
#input_points = generate_circle_dist(num_points, 10000, (10000,10000))

num_points = len(input_points) + 1

start_time = time.time()
quickhull_results = quickhull(input_points)
qh_time = time.time() - start_time

start_time = time.time()
monotone_results = monotone_chain(input_points)
monotone_time = time.time() - start_time

start_time = time.time()
grahm_results = grahm_scan(input_points)
grahm_time = time.time() - start_time

print("*** Number of input points: " + str(num_points))
print("* Quickhull time: " + str(qh_time))
print(sorted(quickhull_results))
print("* Monotone Chain time: " + str(monotone_time))
print(sorted(monotone_results))
print("* Grahm Scan time: " + str(grahm_time))
print(sorted(grahm_results))
