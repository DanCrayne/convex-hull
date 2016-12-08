import math
import random

def generate_random_dist(num_points, min_coord, max_coord):
    points = []

    for i in range(1,num_points):
       points.append((random.randint(min_coord,max_coord),\
                      random.randint(min_coord,max_coord))) 

    return points

def generate_square_dist(num_points, min_coord, max_coord):
    points = []

    generate_random_dist(num_points, min_coord, max_coord)
    # bottom-left corner of square
    points.append((min_coord, min_coord))
    # bottom-right corner of square
    points.append((max_coord, min_coord))
    # top-left corner of square
    points.append((min_coord, max_coord))
    # top-right corner of square
    points.append((max_coord, max_coord))

    return points

def generate_skewed_dist(num_points, min_coord, max_coord):
    points = []

    return generate_random_dist(num_points, min_coord + \
                                (max_coord*0.90), max_coord)

def generate_circle_dist(num_points, radius, center):
    points = []
 
    for i in range(1,num_points):
        # random angle
        alpha = 2 * math.pi * random.random()
        # random radius
        r = radius * random.random()
        # calculating coordinates
        x = r * math.cos(alpha) + center[0]
        y = r * math.sin(alpha) + center[1]
        points.append((math.ceil(x), math.ceil(y)))

    return points
