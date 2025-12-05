import bisect


def prepare_data(data: str) -> tuple[list[tuple[int, int]], list[int]]:
    """Parses the data and normalises it."""
    lines = data.splitlines()

    # split the data into ranges and numbers
    ranges = []
    for i, line in enumerate(lines):
        if not line:
            numbers_start = i + 1
            break
        left, right = line.split("-")
        ranges.append([int(left), int(right)])

    numbers = [int(line) for line in lines[numbers_start:]]

    # sort and merge the ranges
    ranges.sort()
    merge_ranges(ranges)

    return ranges, numbers


def merge_ranges(ranges: list[list[int]]) -> None:
    """Merges sorted ranges."""
    i = 0
    while i < len(ranges) - 1:
        cur_range, next_range = ranges[i], ranges[i + 1]
        if cur_range[1] >= next_range[0]:  # ranges overlap
            cur_range[1] = max(cur_range[1], next_range[1])
            del ranges[i + 1]
        else:
            i += 1


def worker(ranges: list[list[int]], numbers: list[int]) -> int:
    result = 0

    for n in numbers:
        # binary search for a range
        idx = bisect.bisect_right(ranges, n, key=lambda x: x[0])
        if idx == 0:
            continue
        left, right = ranges[idx - 1]
        result += (left <= n <= right)

    return result


def test():
    data = (
        "3-5\n"
        "10-14\n"
        "16-20\n"
        "12-18\n"
        "\n"
        "1\n"
        "5\n"
        "8\n"
        "11\n"
        "17\n"
        "32\n"
        ""
    )
    expected = 3
    ranges, numbers = prepare_data(data)
    result = worker(ranges, numbers)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./5/input.txt") as f:
        data = f.read()

    ranges, numbers = prepare_data(data)
    return worker(ranges, numbers)


if __name__ == "__main__":
    test()
    print(main())
