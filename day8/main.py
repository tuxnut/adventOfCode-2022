import itertools
import os
import sys
from typing import List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


def create_up_of_position(ver: int, hor: int, matrix: List[List[int]]) -> List[int]:
    return [matrix[x][hor] for x in range(ver)]


def create_down_of_position(ver: int, hor: int, matrix: List[List[int]]) -> List[int]:
    length = len(matrix)
    return [matrix[x][hor] for x in range(ver + 1, length)]


def create_left_of_position(ver: int, hor: int, matrix: List[List[int]]) -> List[int]:
    return [matrix[ver][y] for y in range(hor)]


def create_right_of_position(ver: int, hor: int, matrix: List[List[int]]) -> List[int]:
    width = len(matrix[hor])
    return [matrix[ver][y] for y in range(hor + 1, width)]


def is_tree_visible(tree_height: int, top: List[int], down: List[int], left: List[int], right: List[int]) -> bool:
    return tree_height > max(top) or tree_height > max(down) or tree_height > max(left) or tree_height > max(right)


def solve_problem_1(file_content: List[str]):
    matrix = [[int(tree) for tree in list(line.strip())] for line in file_content]
    length = len(matrix)
    width = len(matrix[0])

    number_of_visible_trees = 2 * (length + width - 2)
    for vertical, horizontal in itertools.product(range(1, length - 1), range(1, width - 1)):
        tree_height = matrix[vertical][horizontal]
        top = create_up_of_position(vertical, horizontal, matrix)
        down = create_down_of_position(vertical, horizontal, matrix)
        left = create_left_of_position(vertical, horizontal, matrix)
        right = create_right_of_position(vertical, horizontal, matrix)

        if is_tree_visible(tree_height, top, down, left, right):
            number_of_visible_trees += 1
    return number_of_visible_trees


def create_viewing_up_of_position(ver: int, hor: int, matrix: List[List[int]]) -> int:
    number_of_viewable_trees = 0
    tree_height = matrix[ver][hor]
    for x in range(ver - 1, -1, -1):
        number_of_viewable_trees += 1
        if tree_height <= matrix[x][hor]:
            break

    return number_of_viewable_trees


def create_viewing_down_of_position(ver: int, hor: int, matrix: List[List[int]]) -> int:
    number_of_viewable_trees = 0
    tree_height = matrix[ver][hor]
    length = len(matrix)
    for x in range(ver + 1, length):
        number_of_viewable_trees += 1
        if tree_height <= matrix[x][hor]:
            break

    return number_of_viewable_trees


def create_viewing_left_of_position(ver: int, hor: int, matrix: List[List[int]]) -> int:
    number_of_viewable_trees = 0
    tree_height = matrix[ver][hor]
    for y in range(hor - 1, -1, -1):
        number_of_viewable_trees += 1
        if tree_height <= matrix[ver][y]:
            break

    return number_of_viewable_trees


def create_viewing_right_of_position(ver: int, hor: int, matrix: List[List[int]]) -> int:
    number_of_viewable_trees = 0
    tree_height = matrix[ver][hor]
    width = len(matrix[hor])
    for y in range(hor + 1, width):
        number_of_viewable_trees += 1
        if tree_height <= matrix[ver][y]:
            break

    return number_of_viewable_trees


def solve_problem_2(file_content: List[str]):
    matrix = [[int(tree) for tree in list(line.strip())] for line in file_content]
    length = len(matrix)
    width = len(matrix[0])
    max_scenic_score = 0

    for vertical, horizontal in itertools.product(range(length), range(width)):
        top = create_viewing_up_of_position(vertical, horizontal, matrix)
        down = create_viewing_down_of_position(vertical, horizontal, matrix)
        left = create_viewing_left_of_position(vertical, horizontal, matrix)
        right = create_viewing_right_of_position(vertical, horizontal, matrix)

        scenic_score = top * down * left * right
        max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"Nombre d'arbres visibles {result}")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"{result}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
