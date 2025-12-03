def test():
    data = (
        "987654321111111\n" "811111111111119\n" "234234234234278\n" "818181911112111\n"
    )
    expected = 357
    result = worker(data)
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./3/input.txt") as f:
        data = f.read()
    return worker(data)


def worker(data: str):
    result = 0

    for s in data.split("\n"):
        if not s:
            break
        a, b = s[-2:]

        for i in range(len(s) - 3, -1, -1):
            c = s[i]

            if c >= a:
                b = max(a, b)
                a = c
                if a == "9" and b == "9":
                    break
        
        result += int(a + b)

    return result


if __name__ == "__main__":
    test()
    print(main())
