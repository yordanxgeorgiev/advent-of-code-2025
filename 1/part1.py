def test():
    data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
    expected = 3
    result = worker(data)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./1/input.txt") as f:
        data = f.read()
    return worker(data)


def worker(data: str):
    cur = 50
    count = 0
    for instruction in data.split("\n"):
        if not instruction:
            break
        direction = 1 if instruction[0] == "R" else -1
        rotation = int(instruction[1:][-2:])

        cur += direction * rotation
        if cur < 0 or cur > 99:
            cur -= direction * 100
        if cur == 0:
            count += 1

    return count


if __name__ == "__main__":
    test()
    print(main())