import os
import sys
from typing import List

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

POINTS_FOR_A_WIN = 6
POINTS_FOR_A_DRAW = 3
POINTS_FOR_A_LOSS = 0


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def decrypt_opponent_choice(choice: str) -> str:
    if choice == "A":
        return ROCK
    elif choice == "B":
        return PAPER

    return SCISSORS


def decrypt_own_choice_part_one(choice: str) -> str:
    if choice == "X":
        return ROCK
    elif choice == "Y":
        return PAPER

    return SCISSORS


def decrypt_own_choice_part_two(opponent_choice: str, result: str) -> str:
    if opponent_choice == "A" and result == "X":
        return SCISSORS
    elif opponent_choice == "A" and result == "Y":
        return ROCK
    elif opponent_choice == "A" and result == "Z":
        return PAPER
    elif opponent_choice == "B" and result == "X":
        return ROCK
    elif opponent_choice == "B" and result == "Y":
        return PAPER
    elif opponent_choice == "B" and result == "Z":
        return SCISSORS
    elif opponent_choice == "C" and result == "X":
        return PAPER
    elif opponent_choice == "C" and result == "Y":
        return SCISSORS
    return ROCK


def compute_choice_points(choice: str) -> int:
    if choice == ROCK:
        return 1
    elif choice == PAPER:
        return 2

    return 3


def compute_points(opponent_choice: str, own_choice: str) -> int:
    if (
        (own_choice == ROCK and opponent_choice == SCISSORS)
        or (own_choice == PAPER and opponent_choice == ROCK)
        or (own_choice == SCISSORS and opponent_choice == PAPER)
    ):
        return POINTS_FOR_A_WIN

    if own_choice == opponent_choice:
        return POINTS_FOR_A_DRAW

    else:
        return POINTS_FOR_A_LOSS


def compute_round_score(round: str, problem_part: int) -> int:
    opponent_choice = decrypt_opponent_choice(round[0])
    own_choice = decrypt_own_choice_part_one(round[2]) if problem_part == 1 else decrypt_own_choice_part_two(round[0], round[2])

    return compute_choice_points(own_choice) + compute_points(opponent_choice, own_choice)


def compute_total_score(file_content: List[str], problem_part: int) -> int:
    return sum(compute_round_score(line, problem_part) for line in file_content)


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        total_score = compute_total_score(content, 1)
        print(f"The total score of the game is {total_score}.")
    elif argv == "2":
        total_score = compute_total_score(content, 2)
        print(f"The total score of the game is {total_score}.")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
