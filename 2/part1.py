def test():
    data = (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,"
        "446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    )
    expected = 1227775554
    result = worker(data)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./2/input.txt") as f:
        data = f.read()
    return worker(data)


def worker(data: str):
    result = 0

    for str_range in data.split(","):
        a, b = str_range.split("-")
        a, b = int(a), int(b)

        for i in range(a, b + 1):
            x = str(i)
            if len(x) & 1:
                continue
            if x[:len(x) // 2] == x[len(x) // 2:]:
                result += i

    return result


if __name__ == "__main__":
    test()
    print(main())
