# For this task we basically have to count the number of paths from the start to the
# last row of the grid, which is the number of beams that reach the end.
# (because each split of a beam creates 2 new paths)


def solve(grid: list[list[str]]) -> int:
    start_col = len(grid[0]) // 2
    beams = {start_col: 1}

    for row_idx in range(2, len(grid), 2):
        for beams_idx, beams_count in list(beams.items()):
            if grid[row_idx][beams_idx] == "^":
                beams[beams_idx - 1] = beams.get(beams_idx - 1, 0) + beams_count
                beams[beams_idx + 1] = beams.get(beams_idx + 1, 0) + beams_count
                del beams[beams_idx]

    return sum(beams.values())


def main():
    with open("./7/input.txt") as f:
        data = f.read()

    data = [list(d) for d in data.splitlines()]
    return solve(data)


if __name__ == "__main__":
    print(main())
