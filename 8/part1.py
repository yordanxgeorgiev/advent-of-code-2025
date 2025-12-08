import heapq
import math
from utils.disjoint_set import DisjointSet
import functools
import operator


def get_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def solve(points: list[list[int]], n_closest_pairs: int) -> int:
    heap = []

    # find the distance between each pair of points and add to priority queue
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            distance = get_distance(points[i], points[j])
            heapq.heappush(heap, (distance, i, j))

    # add N closest pairs to a disjoint set
    disjoint_set = DisjointSet[int]()
    for dist, i, j in heapq.nsmallest(n_closest_pairs, heap):
        disjoint_set.union(i, j)

    # find the 3 biggest components in the disjoint set
    component_sizes = []
    for component in disjoint_set.get_components():
        component_size = disjoint_set.get_component_size(component)
        heapq.heappush(component_sizes, component_size)

    largest_components = heapq.nlargest(3, component_sizes)
    return functools.reduce(operator.mul, largest_components)


def main():
    with open("./8/input.txt") as f:
        data = f.readlines()

    points = [[int(n) for n in row.split(",")] for row in data]
    return solve(points, n_closest_pairs=1000)


if __name__ == "__main__":
    print(main())
