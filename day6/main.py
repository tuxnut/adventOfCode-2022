import os
import sys
from typing import List

START_OF_PACKET_LENGTH = 4
START_OF_MESSAGE_LENGTH = 14


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def is_start_of_packet(marker: str) -> bool:
    return len(set(list(marker))) == START_OF_PACKET_LENGTH


def find_start_of_packet_marker(signal: str) -> int:
    for i in range(len(signal) - START_OF_PACKET_LENGTH):
        marker = signal[i : i + START_OF_PACKET_LENGTH]
        if is_start_of_packet(marker):
            return i + START_OF_PACKET_LENGTH

    return len(signal)


def is_start_of_message(marker: str) -> bool:
    return len(set(list(marker))) == START_OF_MESSAGE_LENGTH


def find_start_of_message_marker(signal: str) -> int:
    for i in range(len(signal) - START_OF_MESSAGE_LENGTH):
        marker = signal[i : i + START_OF_MESSAGE_LENGTH]
        if is_start_of_message(marker):
            return i + START_OF_MESSAGE_LENGTH

    return len(signal)


def solve_problem_1(file_content: List[str]) -> int:
    signal = file_content[0]
    return find_start_of_packet_marker(signal)


def solve_problem_2(file_content: List[str]):
    signal = file_content[0]
    return find_start_of_message_marker(signal)


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"Start of packet marker appears at {result}")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"Start of message marker appears at {result}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
