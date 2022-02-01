import math

from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    tr1_01 = ((coords_1[1][0] - coords_1[0][0]) ** 2 + (coords_1[1][1] - coords_1[0][1]) ** 2) ** 0.5
    tr1_12 = ((coords_1[2][0] - coords_1[1][0]) ** 2 + (coords_1[2][1] - coords_1[1][1]) ** 2) ** 0.5
    tr1_20 = ((coords_1[0][0] - coords_1[2][0]) ** 2 + (coords_1[0][1] - coords_1[2][1]) ** 2) ** 0.5

    tr2_01 = ((coords_2[1][0] - coords_2[0][0]) ** 2 + (coords_2[1][1] - coords_2[0][1]) ** 2) ** 0.5
    tr2_12 = ((coords_2[2][0] - coords_2[1][0]) ** 2 + (coords_2[2][1] - coords_2[1][1]) ** 2) ** 0.5
    tr2_20 = ((coords_2[0][0] - coords_2[2][0]) ** 2 + (coords_2[0][1] - coords_2[2][1]) ** 2) ** 0.5

    y1_01_12 = float('{:.3f}'.format(math.acos((tr1_01 ** 2 + tr1_12 ** 2 - tr1_20 ** 2) / (2 * tr1_01 * tr1_12))))
    y1_12_20 = float('{:.3f}'.format(math.acos((tr1_12 ** 2 + tr1_20 ** 2 - tr1_01 ** 2) / (2 * tr1_12 * tr1_20))))
    y1_01_20 = float('{:.3f}'.format(math.acos((tr1_01 ** 2 + tr1_20 ** 2 - tr1_12 ** 2) / (2 * tr1_01 * tr1_20))))

    y2_01_12 = float('{:.3f}'.format(math.acos((tr2_01 ** 2 + tr2_12 ** 2 - tr2_20 ** 2) / (2 * tr2_01 * tr2_12))))
    y2_12_20 = float('{:.3f}'.format(math.acos((tr2_12 ** 2 + tr2_20 ** 2 - tr2_01 ** 2) / (2 * tr2_12 * tr2_20))))
    y2_01_20 = float('{:.3f}'.format(math.acos((tr2_01 ** 2 + tr2_20 ** 2 - tr2_12 ** 2) / (2 * tr2_01 * tr2_20))))

    tr1_y = {y1_01_12, y1_12_20, y1_01_20}
    tr2_y = {y2_01_12, y2_12_20, y2_01_20}
    # print(tr1_y, tr2_y, tr2_y.difference(tr1_y))

    return True if len(tr2_y.difference(tr1_y)) == 0 else False


print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))
print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]))
print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]))
print(similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]))
print(similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]))
print(similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]))
print(similar_triangles([(-1, 3), (5, 0), (-1, -2)], [(-8, -2), (10, 7), (10, -8)]))
print(similar_triangles([(-1, -1), (-4, 3), (4, -4)], [(-4, 1), (-1, -4), (3, -7)]))


# assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
# assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
# assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
# assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
# assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
# assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'


"""
Best "Clear" Solution:


from itertools import starmap
from sympy.geometry import Point, Polygon, are_similar

def poly(points):
    return Polygon(*starmap(Point, points))

def similar_triangles(coords_1, coords_2):
    return are_similar(poly(coords_1), poly(coords_2))
"""



"""
Best "Speedy" Solution:



from typing import List, Tuple
Coords = List[Tuple[int, int]]

def similar_triangles(c1, c2) -> bool:
# The list of two arrays of the squares of the lengths of the sides of the triangles:
  s = [[(c[k-1][0] - c[k][0]) ** 2 + (c[k-1][1] - c[k][1]) ** 2 for k in range(3)] for c in (c1, c2)]
# If the triangles are similar, then the ratio of the corresponding sides are equal:
  return len(set(sorted(s[0])[i] / sorted(s[1])[i] for i in range(3))) == 1
"""


"""
from sympy.geometry import Point, Polygon, are_similar

...???
"""