import os
import sys
from typing import List, Set, Tuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def divide_items_into_compartments(items: str) -> Tuple[str, str]:
    nb_items_per_compartment = len(items) // 2
    return items[:nb_items_per_compartment], items[nb_items_per_compartment:]


def list_items_types(items: str) -> Set[str]:
    return set(list(items))


def find_common_item_between_two(items_in_the_first_compartment: Set[str], items_in_the_second_compartment: Set[str]) -> str:
    common_items = items_in_the_first_compartment.intersection(items_in_the_second_compartment)
    return common_items.pop()


def find_common_item_between_three(first: Set[str], second: Set[str], third: Set[str]) -> str:
    common_items = first.intersection(second)
    common_items = common_items.intersection(third)
    return common_items.pop()


def get_item_priority(item: str) -> int:
    priority = ord(item) - 96
    return priority if priority > 0 else priority + 58


def solve_problem_1(file_content: List[str]):
    total_priority = 0
    for line in file_content:
        line = line.strip()
        first_compartment, second_compartment = divide_items_into_compartments(line)
        items_in_the_first_compartment = list_items_types(first_compartment)
        items_in_the_second_compartment = list_items_types(second_compartment)
        common_item = find_common_item_between_two(items_in_the_first_compartment, items_in_the_second_compartment)
        item_priority = get_item_priority(common_item)
        total_priority += item_priority

    return total_priority


def solve_problem_2(file_content: List[str]):
    total_priority = 0
    group_size = 3
    for i in range(0, len(file_content), group_size):
        first_rucksack = list_items_types(file_content[i].strip())
        second_rucksack = list_items_types(file_content[i + 1].strip())
        third_rucksack = list_items_types(file_content[i + 2].strip())
        common_item = find_common_item_between_three(first_rucksack, second_rucksack, third_rucksack)
        item_priority = get_item_priority(common_item)
        total_priority += item_priority

    return total_priority


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"The sum of priority of the common items is {result}")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"The sum of priority of the common items is {result}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
