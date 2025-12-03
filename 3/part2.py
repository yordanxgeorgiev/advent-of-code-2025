from typing import Iterable


def test():
    data = (
        "987654321111111\n" "811111111111119\n" "234234234234278\n" "818181911112111\n"
    )
    expected = 3121910778619
    result = worker(data.split("\n"))
    if result != expected:
        print(f"result: {result}, expected: {expected}")
    assert result == expected


def main():
    with open("./3/input.txt") as f:
        return worker(f)


def worker(data: Iterable[str]):
    result = 0

    for s in data:
        if not s:
            break
        s = s.rstrip("\n")

        cur = list(s[-12:])

        for i in range(len(s) - 13, -1, -1):
            c = s[i]

            if c >= cur[0]:
                prev = cur[0]
                cur[0] = max(cur[0], c)

                for j in range(1, 12):
                    if prev >= cur[j]:
                        prev, cur[j] = cur[j], prev
                    else:
                        break

        result += int("".join(cur))

    return result


if __name__ == "__main__":
    test()
    print(main())
