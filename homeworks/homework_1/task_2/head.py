import argparse
from typing import List


def print_head(file_names: List[str], rows_number: int = 10):
    print_file_name = len(file_names) > 1
    for file_name in file_names:
        try:
            with open(file_name) as f:
                if print_file_name:
                    print(f"==> {file_name} <==")
                for line_index, line in enumerate(f, start=1):
                    if line_index > rows_number:
                        break
                    print(line, end="")
        except FileNotFoundError:
            print(f"No such file: {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="Quantity of lines", default=10)
    parser.add_argument("files", type=str, nargs="+", help="List of files")
    args = parser.parse_args()
    print_head(args.files, args.n)
