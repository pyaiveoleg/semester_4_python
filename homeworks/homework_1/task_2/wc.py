import argparse
import os
from typing import List


def print_wordstats(file_names: List[str]):
    total_lines = 0
    total_words = 0
    total_bytes = 0

    for file_name in file_names:
        try:
            with open(file_name) as f:
                file_text = f.readlines()
                lines = len(file_text)
                words = sum(len(line.split(" ")) for line in file_text)
                bytes = os.path.getsize(file_name)

                total_lines += lines
                total_words += words
                total_bytes += bytes
                print(f"{lines} {words} {bytes} {file_name}")
        except FileNotFoundError:
            print(f"No such file: {file_name}")

    print(f"{total_lines} {total_words} {total_bytes} итого")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar="", type=str, nargs="+", help="List of files")
    args = parser.parse_args()
    print_wordstats(args.files)
