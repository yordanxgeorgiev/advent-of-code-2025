import heapq
from .part1 import parse_data


wires = []
max_wire_len = 0


class JoltageState:

    def __init__(self, joltage: list[int], level: int):
        self.joltage = joltage
        self.level = level
        self._heuristic = None

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __eq__(self, other):
        return self.joltage == other.joltage

    def __hash__(self):
        return hash(self.joltage)

    def heuristic(self) -> int:
        """Estimates how close this state is to the solution."""
        # the idea is the min possible solution is if we pick the max length wire
        # until we reach the result
        remaining = sum(self.joltage)
        return (remaining + max_wire_len - 1) // max_wire_len

    def fitness(self) -> int:
        """How fit this state is to be the optimal solution, smaller numbers are better."""
        return self.level + self.heuristic()

    def press_button(self, wire: tuple[int]):
        """Simulates using the given wire to toggle some lights, results in a new state."""
        new_joltage = list(self.joltage)
        for pos in wire:
            x = new_joltage[pos]
            if x == 0:
                return False
            new_joltage[pos] = x - 1

        state = JoltageState(joltage=tuple(new_joltage), level=self.level + 1)
        return state


def solve_single(data: dict) -> int:
    global wires
    global max_wire_len

    wires = data["wiring"]
    max_wire_len = max(len(w) for w in wires)
    joltage = tuple(data["joltage"])

    queue = [JoltageState(joltage, level=0)]
    visited = {}

    while queue:
        state = heapq.heappop(queue)
        if all(x == 0 for x in state.joltage):
            return state.level
        if state.joltage in visited and visited[state.joltage] <= state.level:
            continue
        visited[state.joltage] = state.level

        for wire in wires:
            new_state = state.press_button(wire)
            if new_state:
                heapq.heappush(queue, new_state)


def solve(data: list[dict]) -> int:
    result = 0
    for row in data:
        result += solve_single(row)

    return result


def main():
    with open("./10/input.txt") as f:
        data = f.read()

    data = parse_data(data)
    return solve(data)


if __name__ == "__main__":
    print(main())
