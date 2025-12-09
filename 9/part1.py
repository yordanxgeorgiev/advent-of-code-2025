
def worker(points: list[list[int]]):
    max_area = 0

    for i in range(len(points)-1):
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                max_area = area

    return max_area


def main():
    with open("./9/input.txt") as f:
        data = f.read()

    parsed_data = [
        [int(s) for s in str_point.split(",", 1)]
        for str_point in data.splitlines()
    ]
    return worker(parsed_data)


if __name__ == "__main__":
    print(main())
