import argparse
from typing import List


def enumerate_lines(file_names: List[str]):
    line_number = 1
    for file_name in file_names:
        try:
            with open(file_name) as f:
                for line in f:
                    if line.strip():
                        print(f"{line_number}\t{line}", end="")
                        line_number += 1
                    else:
                        print(line, end="")
        except FileNotFoundError:
            print(f"No such file: {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, nargs="+", help="List of files")
    args = parser.parse_args()
    enumerate_lines(args.files)
