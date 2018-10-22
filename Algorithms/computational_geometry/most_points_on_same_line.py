from fractions import Fraction

points = [(-2,-2), (3,-10), (3, 20), (-1,1), (0,4), (2,2), (3,3), (3,-3)]

def most_points_on_same_line(points):
    associations = dict()
    for i, p1 in enumerate(points):
        for p2 in points[i + 1:]:
            m = None if p1[0] == p2[0] else Fraction(p1[1]-p2[1], p1[0]-p2[0])
            b = p1[0] if m == None else (-1 * m * p1[0]) + p1[1]
            if (m, b) not in associations:
                associations[(m, b)] = set()
            associations[(m, b)].add(p1)
            associations[(m, b)].add(p2)
    return associations


if __name__ == '__main__':
    a = most_points_on_same_line(points)
    print(max([ len(v) for v in a.values() ]))
