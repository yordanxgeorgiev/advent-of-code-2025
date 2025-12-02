def test():
    data = (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,"
        "446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    )
    expected = 4174379265
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
            if has_repeating_subsequence(x):
                result += i

    return result


def has_repeating_subsequence(s: str, subseq_len: None | int = None) -> bool:
    if subseq_len is None:
        subseq_len = len(s) // 2
    if subseq_len < 1:
        return False
    if len(s) % subseq_len:
        return has_repeating_subsequence(s, subseq_len-1)

    subsequences_count = len(s) // subseq_len
    subsequence = s[:subseq_len]

    for i in range(1, subsequences_count):
        if subsequence != s[i*subseq_len:(i+1)*subseq_len]:
            return has_repeating_subsequence(s, subseq_len-1)

    return True


if __name__ == "__main__":
    test()
    print(main())
