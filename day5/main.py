import os
import re
import sys
from typing import Dict, List, Tuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def parse_initial_state(file_content: List[str], number_of_columns: int) -> Dict[str, str]:
    state = {}
    file_content.reverse()
    for column in range(number_of_columns):
        column_name = str(column + 1)
        state[column_name] = ""
        for row in file_content:
            if len(row) >= 1 + (column * 4):
                if crate := row[1 + (column * 4)].strip():
                    state[column_name] += crate

    return state


def parse_instructions(line: str) -> Tuple[int, str, str]:
    matches = re.findall(r"\d+", line)
    number_of_crates_to_move = int(matches[0])
    source = str(matches[1])
    destination = str(matches[2])
    return number_of_crates_to_move, source, destination


def remove_crates_from_column(state: Dict[str, str], number_of_crates_to_move: int, source: str) -> Tuple[Dict[str, str], str]:
    column = state.get(source, "")
    removed_crates = column[-number_of_crates_to_move:]
    new_state = {**state, source: column[:-number_of_crates_to_move]}
    return new_state, removed_crates


def place_crates_into_column(state: Dict[str, str], crates: str, destination: str) -> Dict[str, str]:
    return {
        **state,
        destination: state.get(destination, "") + crates,
    }


def reverse_crates(crates: str):
    return crates[::-1]


def move_crates_from_instruction(state: Dict[str, str], line: str, crates_are_to_be_reversed: bool) -> Dict[str, str]:
    number_of_crates_to_move, source, destination = parse_instructions(line)
    state_with_crate_removed, removed_crates = remove_crates_from_column(state, number_of_crates_to_move, source)
    crates_to_replace = reverse_crates(removed_crates) if crates_are_to_be_reversed else removed_crates
    return place_crates_into_column(state_with_crate_removed, crates_to_replace, destination)


def solve_problem_1(file_content: List[str]):
    titi = file_content[:8]
    state = parse_initial_state(titi, 9)
    for line in file_content[10:]:
        line = line.strip()
        if line.startswith("move"):
            state = move_crates_from_instruction(state, line, crates_are_to_be_reversed=True)

    return "".join([crates[-1] for crates in state.values()])


def solve_problem_2(file_content: List[str]):
    state = parse_initial_state(file_content[:8], 9)
    for line in file_content[10:]:
        line = line.strip()
        if line.startswith("move"):
            state = move_crates_from_instruction(state, line, crates_are_to_be_reversed=False)

    return "".join([crates[-1] for crates in state.values()])


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"Crates that end up on the top are {result}")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"Crates that end up on the top are {result}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
