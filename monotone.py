from geometric_fns import *

def monotone_chain(points):
    upper_hull = []
    lower_hull = []

    # sort points lexicographically
    points.sort()

    i = 0
    while i < (len(points)):
        while len(lower_hull) >= 2 and \
              determinant(lower_hull[-2], lower_hull[-1], points[i]) <= 0:
            lower_hull.pop()

        lower_hull.append(points[i])
        i = i + 1

    i = len(points) - 1
    while i >= 0:
        while len(upper_hull) >= 2 and \
              determinant(upper_hull[-2], upper_hull[-1], points[i]) <= 0:
            upper_hull.pop()

        upper_hull.append(points[i])
        i = i - 1


#    for point in points:
#        while len(lower_hull) >= 2 and \
#              determinant(lower_hull[-2], lower_hull[-1], point) <= 0:
#            lower_hull.pop()

#        lower_hull.append(point)
#        print(lower_hull)

#    for point in reversed(points):
#        while len(upper_hull) >= 2 and \
#              determinant(upper_hull[-2], upper_hull[-1], point) <= 0:
#            upper_hull.pop()

#        upper_hull.append(point)
#        print(upper_hull)

    # Remove the first and last elements, as they are included in 
    # the lower hull already.
    upper_hull.pop()
    upper_hull.pop(0)

    return upper_hull + lower_hull
