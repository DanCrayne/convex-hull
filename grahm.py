from geometric_fns import *
from math import *

def grahm_scan(points):
    # sort points by angle from point with lowest x coordinate
#    print("Points before sort: " + str(points))
    
    bottom_point = points[0]

    # find point with lowest x coordinate in O(n) time.
    for point in points:
        if point[1] < bottom_point[1]:
            bottom_point = point

#    print("Bottom point: " + str(bottom_point))

    points_with_angles = get_angles(bottom_point, points)
    points_with_angles.sort(key=lambda point: point[1])
#    print(points_with_angles)
    sorted_points = []
    for point in points_with_angles:
        sorted_points.append(point[0])

#    print("Sorted points: " + str(sorted_points))
    convex_hull = []
#    convex_hull = sorted(points, key=lambda point: point[1])

    for point in sorted_points:
        while len(convex_hull) >= 2 and \
              determinant(convex_hull[-2], convex_hull[-1], point) <= 0:
            convex_hull.pop()

        convex_hull.append(point)
#        print(convex_hull)

    return convex_hull

def get_angles(p0, points):
    angle_list = []

    for point in points:
        angle_list.append((point, get_angle(p0, point)))

    return angle_list

def get_angle(p1, p2):
    return cartesian_angle(float(p2[0]) - float(p1[0]),\
                           float(p2[1]) - float(p1[1]))

# adapted from http://www.algomation.com/algorithm/graham-scan-convex-hull
def cartesian_angle(x, y):
    if (x > 0 and y > 0):
        return math.atan(y / x)
    elif (x < 0 and y > 0):
        return math.atan(-x / y) + math.pi / 2.0
    elif (x < 0 and y < 0):
        return math.atan(y / x) + math.pi
    elif (x > 0 and y < 0):
        return math.atan(-x / y) + math.pi / 2.0 + math.pi
    elif (x == 0 and y > 0):
        return math.pi / 2.0
    elif (x < 0 and y == 0):
        return math.pi
    elif (x == 0 and y < 0):
        return math.pi / 2.0 + math.pi
    else: return 0
