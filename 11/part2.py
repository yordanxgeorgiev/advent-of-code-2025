graph = {}
reversed_graph = {}


def build_graph(data: str) -> list[dict]:
    graph.clear()
    reversed_graph.clear()

    for line in data.splitlines():
        node, children = line.split(":", 1)
        children = children.split()

        graph[node] = children
        for child in children:
            reversed_graph.setdefault(child, []).append(node)


_cache = {}


def solve(node: str, path: set, dac: bool, fft: bool) -> int:
    key = (node, dac, fft)
    if key in _cache:
        return _cache[(node, dac, fft)]
    if node in path:
        return 0

    if node == "dac":
        dac = True
    elif node == "fft":
        fft = True
    elif node == "out":
        return dac and fft

    path.add(node)

    total = sum(solve(child, path, dac, fft) for child in graph[node])
    _cache[key] = total

    path.remove(node)  # backtrack
    return total


def main():
    with open("./11/input.txt") as f:
        data = f.read()

    build_graph(data)
    return solve("svr", dac=False, fft=False, path=set())


if __name__ == "__main__":
    print(main())
