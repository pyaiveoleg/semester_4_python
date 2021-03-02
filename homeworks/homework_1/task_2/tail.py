import argparse
from typing import List


def print_tail(file_names: List[str], rows_number: int = 10):
    print_file_name = len(file_names) > 1
    for file_name in file_names:
        try:
            with open(file_name) as f:
                if print_file_name:
                    print(f"==> {file_name} <==")
                print("".join(list(f)[-rows_number:]))
        except FileNotFoundError:
            print(f"No such file: {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar="", type=str, nargs="+", help="List of files")
    args = parser.parse_args()
    print_tail(args.files)
