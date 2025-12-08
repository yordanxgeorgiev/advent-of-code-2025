import heapq
from .part1 import get_distance
from utils.disjoint_set import DisjointSet


def solve(points: list[list[int]]) -> int:
    heap = []
    disjoint_set = DisjointSet[int]()

    # find the distance between each pair of points and add to priority queue
    # and to a disjoint set where each point is its own component
    for i in range(len(points) - 1):
        disjoint_set.add(i)
        for j in range(i + 1, len(points)):
            distance = get_distance(points[i], points[j])
            heapq.heappush(heap, (distance, i, j))

    # union the min distance pair points until the set is no longer disjoint
    while disjoint_set.components_count > 1:
        dist, i, j = heapq.heappop(heap)
        disjoint_set.union(i, j)

    return points[i][0] * points[j][0]


def main():
    with open("./8/input.txt") as f:
        data = f.readlines()

    points = [[int(n) for n in row.split(",")] for row in data]
    return solve(points)


if __name__ == "__main__":
    print(main())
