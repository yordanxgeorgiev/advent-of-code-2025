import json
import requests


def get_inputs(day: int):
    url = f"https://adventofcode.com/2025/day/{day}/input"

    with open("./secrets.json", "r") as f:
        secrets = json.load(f)

    content = requests.get(
        url, cookies={"session": secrets["session_id"]}
    ).content.decode()

    with open(f"./{day}/input.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    get_inputs(day=1)