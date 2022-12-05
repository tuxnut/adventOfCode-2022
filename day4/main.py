import os
import sys
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Range:
    start: int
    end: int


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def parse_ranges(line: str) -> Tuple[Range, Range]:
    ranges = line.split(",")
    first_range_raw = ranges[0]
    second_range_raw = ranges[1]
    first_range_bounds = first_range_raw.split("-")
    second_range_bounds = second_range_raw.split("-")
    first_range = Range(int(first_range_bounds[0]), int(first_range_bounds[1]))
    second_range = Range(int(second_range_bounds[0]), int(second_range_bounds[1]))
    return first_range, second_range


def is_one_range_fully_containing_the_other(first_range: Range, second_range: Range) -> bool:
    first_range_is_fully_containing_the_second = first_range.start <= second_range.start and first_range.end >= second_range.end
    second_range_is_fully_containing_the_first = second_range.start <= first_range.start and second_range.end >= first_range.end
    return first_range_is_fully_containing_the_second or second_range_is_fully_containing_the_first


def are_pairs_overlapping(first_range: Range, second_range: Range) -> bool:
    if first_range.end < second_range.start:
        return False

    if first_range.start > second_range.end:
        return False

    return True


def solve_problem_1(file_content: List[str]):
    assignment_with_a_pair_fully_containing_the_other = 0
    for line in file_content:
        line = line.strip()
        first_range, second_range = parse_ranges(line)
        if is_one_range_fully_containing_the_other(first_range, second_range):
            assignment_with_a_pair_fully_containing_the_other += 1

    return assignment_with_a_pair_fully_containing_the_other


def solve_problem_2(file_content: List[str]):
    assignment_with_overlapping_pairs = 0
    for line in file_content:
        line = line.strip()
        first_range, second_range = parse_ranges(line)
        if are_pairs_overlapping(first_range, second_range):
            print(f"{first_range=}")
            print(f"{second_range=}")
            assignment_with_overlapping_pairs += 1
            print()

    return assignment_with_overlapping_pairs


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"{result}")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"{result}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
