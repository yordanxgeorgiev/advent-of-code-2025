from .part1 import prepare_data


def worker(ranges: list[list[int]], numbers: list[int]) -> int:
    result = 0

    for _range in ranges:
        result += _range[1] - _range[0] + 1

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
    expected = 14
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
