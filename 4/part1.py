from typing import Iterator


def test():
    data = (
        "..@@.@@@@.\n"
        "@@@.@.@.@@\n"
        "@@@@@.@.@@\n"
        "@.@@@@..@.\n"
        "@@.@@@@.@@\n"
        ".@@@@@@@.@\n"
        ".@.@.@.@@@\n"
        "@.@@@.@@@@\n"
        ".@@@@@@@@.\n"
        "@.@.@@@.@.\n"
    )
    expected = 13
    result = worker(data)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./4/input.txt") as f:
        data = f.read()
    return worker(data)


def get_neighbour_positions(
    i: int, j: int, max_i: int, max_j: int
) -> Iterator[tuple[int, int]]:
    """Returns the neighbour positions around (i, j)."""
    for k in range(-1, 2):
        for m in range(-1, 2):
            if k != 0 or m != 0:
                a, b = i + k, j + m
                if 0 <= a <= max_i and 0 <= b <= max_j:
                    yield a, b


def count_neighbour_rolls(grid: list[list[str]], i: int, j: int) -> int:
    """Counts the number of neighbour rolls (@) around position (i, j)."""
    return sum(
        grid[k][m] == "@"
        for k, m in get_neighbour_positions(i, j, len(grid) - 1, len(grid[0]) - 1)
    )


def worker(data: str):
    grid = [list(row) for row in data.split("\n")[:-1]]
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                count += count_neighbour_rolls(grid, i, j) < 4

    return count


if __name__ == "__main__":
    test()
    print(main())
