import math
from geometric_fns import *

def quickhull(points):
    upper_convex_hull = []
    lower_convex_hull = []

    max_x = points[0]
    min_x = points[0]
    for point in points:
        if point[0] > max_x[0]:
            max_x = point
        if point[0] < min_x[0]:
            min_x = point

    p1 = min_x
    pn = max_x

    upper_points = get_upper_points(points, p1, pn)
    lower_points = get_lower_points(points, p1, pn)

    upper_convex_hull = get_hull(upper_points, p1, pn)
    upper_convex_hull.append(p1)
    upper_convex_hull.append(pn)

    lower_convex_hull = get_hull(lower_points, pn, p1)

    return upper_convex_hull + lower_convex_hull

    
def get_hull(points, p1, pn):
    convex_hull = []
    if not points:
        return convex_hull

    pmax = find_furthest_point_from_line(points, p1, pn)
    convex_hull.append(pmax)
    points1 = find_points_to_left_of_line(points, p1, pmax)
    points2 = find_points_to_left_of_line(points, pmax, pn)
    return convex_hull + get_hull(points1, p1, pmax)\
                       + get_hull(points2, pmax, pn)

def get_lower_points(points, p1, pn):
    lower_points = []

    for point in points:
       if determinant(p1, pn, point) < 0:
            lower_points.append(point)

    return lower_points

def get_upper_points(points, p1, pn):
    upper_points = []

    for point in points:
        if determinant(pn, p1, point) < 0:
            upper_points.append(point)

    return upper_points

def find_points_to_left_of_line(points, line_pt1, line_pt2):
    points_to_left = []

    for point in points:
        if determinant(line_pt1, line_pt2, point) > 0:
            points_to_left.append(point)

    return points_to_left

def find_furthest_point_from_line(points, line_pt1, line_pt2):
    max_point = points[0]
    max_distance = 0

    for point in points:
        # The determinant provides a distance measure
        distance_to_point = abs(determinant(\
                                      line_pt1, line_pt2, point))
        if distance_to_point > max_distance:
            max_distance = distance_to_point
            max_point = point

    return max_point
