graph = {}


def build_graph(data: str) -> list[dict]:
    graph.clear()

    for line in data.splitlines():
        node, children = line.split(":", 1)
        graph[node] = children.split()


def solve(node: str) -> int:
    # dfs
    if node == "out":
        return 1
    return sum(solve(child) for child in graph[node])


def test():
    data = (
        "aaa: you hhh\n"
        "you: bbb ccc\n"
        "bbb: ddd eee\n"
        "ccc: ddd eee fff\n"
        "ddd: ggg\n"
        "eee: out\n"
        "fff: out\n"
        "ggg: out\n"
        "hhh: ccc fff iii\n"
        "iii: out\n"
        ""
    )
    build_graph(data)
    return solve("you")



def main():
    with open("./11/input.txt") as f:
        data = f.read()

    build_graph(data)
    return solve("you")


if __name__ == "__main__":
    print(main())
