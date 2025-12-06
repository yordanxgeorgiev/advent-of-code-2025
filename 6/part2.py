from .part1 import worker as part1_worker


def prepare_data(data: str):
    """Parses the data and normalises it."""
    lines = data.splitlines()
    operators = lines[-1].split()
    numbers = [[] for _ in operators]

    for line in lines[:-1]:
        for i, n in enumerate(line.split()):
            numbers[i].append(int(n))

    return numbers, operators


def worker(numbers: list[list[int]], operators: list[str]) -> int:
    return part1_worker(numbers, operators)


def test():
    data = "123 328  51 64\n" "45 64  387 23\n" "6 98  215 314\n" "*   +   *   + \n" ""
    expected = 3263827
    data = prepare_data(data)
    result = worker(*data)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./6/input.txt") as f:
        data = f.read()

    data = prepare_data(data)
    return worker(*data)


if __name__ == "__main__":
    test()
    print(main())
