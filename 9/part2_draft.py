from typing import List, Tuple


def test():
    data = "7,1\n" "11,1\n" "11,7\n" "9,7\n" "9,5\n" "2,5\n" "2,3\n" "7,3\n" ""
    expected = 24

    parsed_data = [
        [int(s) for s in str_point.split(",", 1)] for str_point in data.splitlines()
    ]
    result = worker(parsed_data)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    # assert result == expected


class Polygon:
    def __init__(self, points: List[List[int]]):
        self.points = points
        self.n = len(points)
        self.cache = {}

        # Precompute edges and bounding box
        self.edges = []
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")

        for i in range(self.n):
            p1 = points[i]
            p2 = points[(i + 1) % self.n]

            x1, y1 = p1
            x2, y2 = p2
            min_x = min(min_x, x1)
            max_x = max(max_x, x1)
            min_y = min(min_y, y1)
            max_y = max(max_y, y1)

            self.edges.append({"p1": p1, "p2": p2})

        self.min_x, self.max_x = min_x, max_x
        self.min_y, self.max_y = min_y, max_y

    @staticmethod
    def _is_left(p1: Tuple[int, int], p2: Tuple[int, int], point: Tuple[int, int]) -> bool:
        x1, y1 = p1
        x2, y2 = p2
        x, y = point
        return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) > 0

    @staticmethod
    def _point_on_segment(p: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        x, y = p
        x1, y1 = a
        x2, y2 = b
        if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
            return False
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    @staticmethod
    def _segments_intersect(p1, p2, q1, q2) -> bool:
        """Check if two segments p1-p2 and q1-q2 intersect"""
        def ccw(a,b,c):
            return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
        return ccw(p1,q1,q2) != ccw(p2,q1,q2) and ccw(p1,p2,q1) != ccw(p1,p2,q2)

    def inside(self, point: List[int]) -> bool:
        px, py = point
        key = (px, py)
        if key in self.cache:
            return self.cache[key]

        if px < self.min_x or px > self.max_x or py < self.min_y or py > self.max_y:
            self.cache[key] = False
            return False

        winding_number = 0
        for edge in self.edges:
            p1 = edge["p1"]
            p2 = edge["p2"]
            if self._point_on_segment((px, py), p1, p2):
                self.cache[key] = True
                return True
            y1, y2 = p1[1], p2[1]
            if y1 <= py < y2:
                if self._is_left(p1, p2, (px, py)):
                    winding_number += 1
            elif y2 <= py < y1:
                if not self._is_left(p1, p2, (px, py)):
                    winding_number -= 1
        inside = winding_number != 0
        self.cache[key] = inside
        return inside

    def rectangle_inside(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """Check if a rectangle is entirely inside the polygon, robustly."""
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        # Quick bounding box check
        if min_x < self.min_x or max_x > self.max_x or min_y < self.min_y or max_y > self.max_y:
            return False

        # Rectangle corners
        corners = [(min_x,min_y), (min_x,max_y), (max_x,min_y), (max_x,max_y)]

        # All corners must be inside
        if not all(self.inside([x, y]) for x, y in corners):
            return False

        # Rectangle edges must not intersect any polygon edge
        rect_edges = [
            (corners[0], corners[1]),
            (corners[1], corners[3]),
            (corners[3], corners[2]),
            (corners[2], corners[0])
        ]

        for r1, r2 in rect_edges:
            for edge in self.edges:
                if self._segments_intersect(r1, r2, edge["p1"], edge["p2"]):
                    return False

        return True



def worker(points: list[list[int]]):
    max_area = 3826070

    p = Polygon(points)
    areas = []

    for i in range(len(points) - 1):
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            areas.append((area, i, j))

    areas.sort()

    for area, i, j in areas:
        if area > max_area:
            print("trying " + str(area))
            x1, y1 = points[i]
            x2, y2 = points[j]
            if p.rectangle_inside(x1, y1, x2, y2):
                max_area = area
                print(max_area)

    return max_area


def main():
    with open("./9/input.txt") as f:
        data = f.read()

    parsed_data = [
        [int(s) for s in str_point.split(",", 1)] for str_point in data.splitlines()
    ]
    return worker(parsed_data)


if __name__ == "__main__":
    print(main())
