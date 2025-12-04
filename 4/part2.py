from .part1 import get_neighbour_positions, count_neighbour_rolls


def main():
    with open("./4/input.txt") as f:
        data = f.read()

    grid = [list(row) for row in data.split("\n")[:-1]]
    return worker(grid)


def is_roll_accessable(grid: list[list[str]], i: int, j: int) -> bool:
    """Checks if the roll at position (i, j) is accessable (has <4 neighbour rolls)."""
    return grid[i][j] == "@" and count_neighbour_rolls(grid, i, j) < 4


def worker(grid: list[list[str]]):
    # we'll do a DFS style approach:
    # - find all positions with <4 neighbour rolls and add to a stack
    # - while the stack is not empty - pop a position, mark it as visited, add its neighbours to the stack
    stack = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_roll_accessable(grid, i, j):
                stack.append((i, j))

    result = 0

    while stack:
        i, j = stack.pop()
        if grid[i][j] == ".":
            continue  # already visited

        grid[i][j] = "."
        result += 1

        # expand to neighbours
        for i, j in get_neighbour_positions(i, j, len(grid) - 1, len(grid[0]) - 1):
            if is_roll_accessable(grid, i, j):
                stack.append((i, j))

    return result


if __name__ == "__main__":
    print(main())
