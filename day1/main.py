import os
import sys
from typing import List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content

def group_calories_by_elves(file_content: list[str]) -> List[int]:
    calories_by_elves = []
    calories = 0
    for line in file_content:
        if line == "\n":
            calories_by_elves.append(calories)
            calories = 0
            continue
        calories += int(line)

    return calories_by_elves

def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        calories_by_elves = group_calories_by_elves(content)
        print(f"The Elf carrying the most calories carries {max(calories_by_elves)} calories.")
    elif argv == "2":
        calories_by_elves = group_calories_by_elves(content)
        calories_by_elves.sort(reverse=True)
        sum_of_calories_of_the_three = sum(calories_by_elves[:3])
        print(f"The 3 Elves carrying the most calories carry {sum_of_calories_of_the_three} calories.")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
