def test():
    data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
    expected = 6
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
        rotation = instruction[1:]
        if len(rotation) > 2:
            count += int(rotation[:-2])
        rotation = int(rotation[-2:])

        x = cur + direction * rotation
        if direction == 1:
            if x >= 100:
                count += 1
                x -= 100
        else:
            if x == 0 or x < 0 and cur > 0:
                count += 1
            if x < 0:
                x += 100
        cur = x

    return count


if __name__ == "__main__":
    test()
    print(main())
