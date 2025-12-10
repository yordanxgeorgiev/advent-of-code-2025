import itertools
import json


def parse_data(data: str) -> list[dict]:
    # the lights array begs to be converted to binary

    parsed_lines = []

    for line in data.splitlines():
        elems = line.split()
        lights = json.loads(
            "[" + ",".join(elems[0][1:-1]).replace(".", "0").replace("#", "1") + "]"
        )
        wiring = json.loads(
            "[" + ",".join(elems[1:-1]).replace("(", "[").replace(")", "]") + "]"
        )
        joltage = json.loads("[" + elems[-1][1:-1] + "]")

        parsed_lines.append(
            {
                "lights": lights,
                "wiring": tuple(wiring),
                "joltage": joltage,
            }
        )

    return parsed_lines


def press_button(lights: list[int], wire: list[int]) -> list[int]:
    """Flips the switches of specified in the wiring."""
    result = lights.copy()
    for pos in wire:
        result[pos] ^= 1
    return result


def solve_single(data: dict) -> int:
    lights = data["lights"]
    wiring = data["wiring"]

    # BFS without revisiting
    cur_lights = [[0 for _ in range(len(lights))]]
    visited = set()

    for i in itertools.count():
        next_lights = []

        while cur_lights:
            lights_state = cur_lights.pop()
            if lights_state == lights:
                return i

            lights_state_tuple = tuple(lights_state)
            if lights_state_tuple in visited:
                continue

            next_lights.extend(press_button(lights_state, wire) for wire in wiring)
            visited.add(lights_state_tuple)

        cur_lights = next_lights


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
