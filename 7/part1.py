def solve(grid: list[list[str]]) -> int:
    result = 0
    start_col = len(grid[0]) // 2
    beams = {start_col}  # unique positions of beams on a single row

    for row_idx in range(2, len(grid), 2):
        for beams_idx in list(beams):
            if grid[row_idx][beams_idx] == "^":
                result += 1
                beams.remove(beams_idx)
                beams.add(beams_idx - 1)
                beams.add(beams_idx + 1)

    return result


def main():
    with open("./7/input.txt") as f:
        data = f.read()

    data = [list(d) for d in data.splitlines()]
    return solve(data)


if __name__ == "__main__":
    print(main())
