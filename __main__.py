#!/usr/bin/env python3

__author__ = "Eryk Darnowski"
__version__ = "0.0.0"
__license__ = "MIT"


def main():
    input_filename = "transcript.txt"
    # read the input file contents
    with open(input_filename, "r", encoding="utf-8") as input_file:
        transcript = input_file.read()


if __name__ == "__main__":
    main()
