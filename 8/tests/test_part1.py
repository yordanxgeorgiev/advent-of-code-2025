from ..part1 import solve


TEST_DATA = (
    "162,817,812\n"
    "57,618,57\n"
    "906,360,560\n"
    "592,479,940\n"
    "352,342,300\n"
    "466,668,158\n"
    "542,29,236\n"
    "431,825,988\n"
    "739,650,466\n"
    "52,470,668\n"
    "216,146,977\n"
    "819,987,18\n"
    "117,168,530\n"
    "805,96,715\n"
    "346,949,466\n"
    "970,615,88\n"
    "941,993,340\n"
    "862,61,35\n"
    "984,92,344\n"
    "425,690,689\n"
    ""
)


def test():
    expected = 40

    points = []
    for row in TEST_DATA.split("\n")[:-1]:
        point = [int(n) for n in row.split(",")]
        points.append(point)

    result = solve(points, n_closest_pairs=10)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


if __name__ == "__main__":
    test()
