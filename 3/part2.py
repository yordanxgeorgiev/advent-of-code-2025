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
    # Idea:
    #
    # let n be a decimal string of length L
    # S(k) = maximum 12-digit subsequence contained in the last k digits of n (n[−k:])
    # - S(12) is the last 12 digits of n (n[-12:])
    # - S(13) is the maximum of:
    #   - S(12)
    #   - the 12-digit number starting with n[-13], followed by the best 11-digit subsequence in n[-12:]
    # ...
    # - S(i) is the maximum of:
    #   - S(i-1)
    #   - the 12-digit number starting with n[-i], followed by the best 11-digit subsequence in n[-i-1:]
    # ...
    # - S(L) = the largest 12-digit subsequence of the full string n
    #
    # (solve S(12) -> S(13) -> ... -> S(L))

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
