import os
import sys
from typing import List, Set, Tuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


class Directory:
    def __init__(self, name: str, parent: "Directory"):
        self.files: List[int] = []
        self.dirs: List["Directory"] = []
        self.name = name
        self.parent = parent

    def add_file(self, file_size: int):
        self.files.append(file_size)

    def add_folder(self, directory: "Directory"):
        self.dirs.append(directory)

    def get_size(self):
        return sum(self.files) + sum(dir.get_size() for dir in self.dirs)

    def __repr__(self) -> str:
        return f"{self.name}: {self.dirs + self.files}"

    def __str__(self) -> str:
        return self.__repr__()

    def __hash__(self) -> int:
        return hash(self.name)


def is_command(line: str) -> bool:
    return line.startswith("$")


def is_listing_command(command: str) -> bool:
    return command.startswith("$ ls")


def is_command_changing_directory(command: str) -> bool:
    return command.startswith("$ cd")


def is_directory(line: str) -> bool:
    return line.startswith("dir")


def get_directory_name(line: str) -> str:
    return line.split(" ")[-1]


def get_file_size(line: str) -> int:
    return int(line.split(" ")[0])


def get_child_directory(directory_name: str, parent_directory: Directory) -> Directory:
    return next((directory for directory in parent_directory.dirs if directory.name == directory_name), parent_directory)


def create_filesystem(file_content) -> Tuple[Directory, Set[Directory]]:
    is_listing = False
    filesystem = Directory("/", None)
    current_parent_directory = filesystem
    directories = {current_parent_directory}
    for line in file_content:
        line = line.rstrip()
        if is_command(line):
            is_listing = False
            if is_command_changing_directory(line):
                directory_name = get_directory_name(line)
                current_parent_directory = (
                    current_parent_directory.parent if directory_name == ".." else get_child_directory(directory_name, current_parent_directory)
                )
            if is_listing_command(line):
                is_listing = True
            continue

        if is_listing:
            if is_directory(line):
                directory_name = get_directory_name(line)
                new_directory = Directory(directory_name, current_parent_directory)
                current_parent_directory.add_folder(new_directory)
                directories.add(new_directory)
            else:
                file_size = get_file_size(line)
                current_parent_directory.add_file(file_size)
    return filesystem, directories


def solve_problem_1(file_content: List[str]):
    filesystem, directories = create_filesystem(file_content)
    directory_sizes = [directory.get_size() for directory in directories]
    return sum(size for size in directory_sizes if size <= 100000)


def solve_problem_2(file_content: List[str]):
    filesystem, directories = create_filesystem(file_content)
    directory_sizes = [directory.get_size() for directory in directories]
    directory_sizes.sort()
    used_memory = directory_sizes[-1]
    space_to_make = 30000000 - (70000000 - used_memory)
    for size in directory_sizes:
        if size > space_to_make:
            return size


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        result = solve_problem_1(content)
        print(f"La somme des dossiers avec une taille <= 100000 est de {result}")
    elif argv == "2":
        result = solve_problem_2(content)
        print(f"La taille du dossier à supprimer permettant la MàJ {result}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
