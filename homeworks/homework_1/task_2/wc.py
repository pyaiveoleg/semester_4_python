import argparse
import os
from typing import List


def print_wordstats(file_names: List[str]):
    total_lines, total_words, total_bytes = 0, 0, 0
    for file_name in file_names:
        try:
            with open(file_name) as f:
                bytes = os.path.getsize(file_name)
                lines, words = 0, 0
                for line in f:
                    lines += 1
                    words += len(line.split())

                total_lines += lines
                total_words += words
                total_bytes += bytes
                print(f"{lines} {words}\t{bytes}\t{file_name}")
        except FileNotFoundError:
            print(f"No such file: {file_name}")
    if len(file_names) > 1:
        print(f"{total_lines}\t{total_words}\t{total_bytes}\tитого")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, nargs="+", help="List of files")
    args = parser.parse_args()
    print_wordstats(args.files)
