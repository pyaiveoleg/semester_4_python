import argparse
from typing import List


def enumerate_lines(file_names: List[str]):
    line_number = 1
    for file_name in file_names:
        try:
            with open(file_name) as f:
                for line in f:
                    print(f"{line_number} {line}", end="")
                    line_number += 1
        except FileNotFoundError:
            print(f"No such file: {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar="", type=str, nargs="+", help="List of files")
    args = parser.parse_args()
    enumerate_lines(args.files)
