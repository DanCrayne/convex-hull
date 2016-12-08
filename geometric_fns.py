import math

# The determinant is used to determine the orientation of a point
# in relation to a line. Normally, p1p2 will be the line, and p3
# will be the point.
# If d = 0 then p3 is on line p1p2
# If d > 0 then p3 is left of line p1p2
# If d < 0 then p3 is right of line p1p2
def determinant(p1, p2, p3):
   x1 = p1[0]
   y1 = p1[1]
   x2 = p2[0]
   y2 = p2[1]
   x3 = p3[0]
   y3 = p3[1]

   return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3
