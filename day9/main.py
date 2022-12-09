import os
import sys
from math import sqrt
from typing import List, Set, Tuple

Position = Tuple[int, int]
UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def parse_motion(motion: str) -> Tuple[str, int]:
    direction, distance = motion.split(" ")
    return direction, int(distance)


def compute_head_position(head_position: Position, direction: str) -> Position:
    if direction == UP:
        return (head_position[0], head_position[1] + 1)
    elif direction == DOWN:
        return (head_position[0], head_position[1] - 1)
    elif direction == LEFT:
        return (head_position[0] - 1, head_position[1])
    else:
        return (head_position[0] + 1, head_position[1])


def compute_tail_position(tail_position: Position, head_position: Position) -> Position:
    distance_between = sqrt((tail_position[0] - head_position[0]) ** 2 + (tail_position[1] - head_position[1]) ** 2)
    if not distance_between > sqrt(2):
        return tail_position

    increment_x = 0
    increment_y = 0
    if head_position[1] > tail_position[1] + 1:
        increment_y = 1
        if distance_between > 2:
            increment_x = 1 if head_position[0] > tail_position[0] else -1
    elif head_position[1] < tail_position[1] - 1:
        increment_y = -1
        if distance_between > 2:
            increment_x = 1 if head_position[0] > tail_position[0] else -1
    elif head_position[0] > tail_position[0] + 1:
        increment_x = 1
        if distance_between > 2:
            increment_y = 1 if head_position[1] > tail_position[1] else -1
    elif head_position[0] < tail_position[0] - 1:
        increment_x = -1
        if distance_between > 2:
            increment_y = 1 if head_position[1] > tail_position[1] else -1

    return (tail_position[0] + increment_x, tail_position[1] + increment_y)


def solve_problem_1(file_content: List[str]):
    visited_positions: Set[Position] = {(0, 0)}
    head_position = tail_position = (0, 0)
    for line in file_content:
        line = line.strip()
        direction, distance = parse_motion(line)

        for _ in range(distance):
            head_position = compute_head_position(head_position, direction)
            tail_position = compute_tail_position(tail_position, head_position)
            visited_positions.add(tail_position)
    return len(visited_positions)


def solve_problem_2(file_content: List[str]):
    visited_positions: Set[Position] = {(0, 0)}
    knot_positions: List[Position] = [(0, 0)] * 10
    for line in file_content:
        line = line.strip()
        direction, distance = parse_motion(line)

        for _ in range(distance):
            knot_positions[0] = compute_head_position(knot_positions[0], direction)
            for index in range(1, len(knot_positions)):
                knot_behind, knot_ahead = knot_positions[index], knot_positions[index - 1]
                knot_positions[index] = compute_tail_position(knot_behind, knot_ahead)

            visited_positions.add(knot_positions[-1])
    return len(visited_positions)


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"The tail visited {result} positions")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"The tail visited {result} positions")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
