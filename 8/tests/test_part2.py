from .test_part1 import TEST_DATA
from ..part2 import solve


def test():
    expected = 25272

    points = []
    for row in TEST_DATA.split("\n")[:-1]:
        point = [int(n) for n in row.split(",")]
        points.append(point)

    result = solve(points)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


if __name__ == "__main__":
    test()
