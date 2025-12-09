import functools


class Polygon:
    def __init__(self, points: list[tuple[int, int]]):
        self.points = points
        self.edges = []

        for i in range(len(points) - 1):
            self.edges.append({"p1": points[i], "p2": points[i + 1]})

        self.edges.append({"p1": points[-1], "p2": points[0]})

    @staticmethod
    def _orient(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
        """Gives the direction of the turn (a, b, c), >0 left turn, <0 right turn, 0 points are collinear."""
        # cross-product of the vectors (a, b) and (a, c)
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    @staticmethod
    def _point_on_segment(
        p: tuple[int, int], a: tuple[int, int], b: tuple[int, int]
    ) -> bool:
        """Is a point on a given line segment (is p in [a, b])."""
        if Polygon._orient(a, b, p) != 0:
            return False

        min_x, max_x = min(a[0], b[0]), max(a[0], b[0])
        min_y, max_y = min(a[1], b[1]), max(a[1], b[1])

        return min_x <= p[0] <= max_x and min_y <= p[1] <= max_y

    @staticmethod
    def _segments_intersect(
        p1: tuple[int, int],
        p2: tuple[int, int],
        q1: tuple[int, int],
        q2: tuple[int, int],
    ) -> bool:
        """Do the two segments p and q intersect."""
        o1 = Polygon._orient(p1, p2, q1)
        o2 = Polygon._orient(p1, p2, q2)
        o3 = Polygon._orient(q1, q2, p1)
        o4 = Polygon._orient(q1, q2, p2)

        # idea here is that if the line p crosses the segment (q1, q2), and the line q
        # crosses the segment (p1, p2), the two segments intersect
        if o1 * o2 < 0 and o3 * o4 < 0:
            return True

        # check for collinearity and intersection at the ends of the segments
        return (
            (o1 == 0 and Polygon._point_on_segment(q1, p1, p2))
            or (o2 == 0 and Polygon._point_on_segment(q2, p1, p2))
            or (o3 == 0 and Polygon._point_on_segment(p1, q1, q2))
            or (o4 == 0 and Polygon._point_on_segment(p2, q1, q2))
        )

    @staticmethod
    def _proper_intersection(
        p1: tuple[int, int],
        p2: tuple[int, int],
        q1: tuple[int, int],
        q2: tuple[int, int],
    ) -> bool:
        """
        Return True only if segments properly cross at interior points (no collinear, no endpoint-touch).
        """
        o1 = Polygon._orient(p1, p2, q1)
        o2 = Polygon._orient(p1, p2, q2)
        o3 = Polygon._orient(q1, q2, p1)
        o4 = Polygon._orient(q1, q2, p2)

        # proper crossing occurs only when orientations are strictly opposite on both sides
        return (o1 * o2 < 0) and (o3 * o4 < 0)

    @functools.lru_cache(maxsize=None)
    def inside(self, point: tuple[int, int]) -> bool:
        """Is a point inside the polygon."""
        px, py = point

        cnt = 0

        # cast a ray to the right of the point and check if the number of edges crossed
        # is even or odd number
        for edge in self.edges:
            x1, y1 = edge["p1"]
            x2, y2 = edge["p2"]

            # on boundary?
            if self._point_on_segment((px, py), (x1, y1), (x2, y2)):
                return True

            # cast ray
            if (y1 > py) != (y2 > py):
                x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
                if px < x_int:
                    cnt ^= 1

        return cnt == 1

    def rectangle_inside(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """Is a rectangle inside the polygon."""
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]

        # all corners must be inside polygon (on-edge counts as inside)
        for c in corners:
            if not self.inside(c):
                return False

        # rectangle edges must not properly intersect polygon edges,
        # but touching or collinear overlap is fine
        rect_edges = [
            (corners[0], corners[1]),
            (corners[1], corners[3]),
            (corners[3], corners[2]),
            (corners[2], corners[0]),
        ]

        for r1, r2 in rect_edges:
            for edge in self.edges:
                if self._proper_intersection(r1, r2, edge["p1"], edge["p2"]):
                    return False

        return True


def solve(points: list[tuple[int, int]]):
    p = Polygon(points)
    areas = []

    # calculate all candidate areas
    for i in range(len(points) - 1):
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            areas.append((area, i, j))

    # starting from the rectangles with the biggest area check if they are inside the polygon
    areas.sort(reverse=True)

    for area, i, j in areas:
        print("Trying rectangle with area: " + str(area))
        if p.rectangle_inside(*points[i], *points[j]):
            return area


def main():
    with open("./9/input.txt") as f:
        data = f.read()

    parsed_data = [
        tuple(int(s) for s in str_point.split(",", 1))
        for str_point in data.splitlines()
    ]
    result = solve(parsed_data)  # type: ignore
    return result


if __name__ == "__main__":
    print(main())
