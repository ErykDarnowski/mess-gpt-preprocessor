#!/usr/bin/env python3

import re

__author__ = "Eryk Darnowski"
__version__ = "0.0.0"
__license__ = "MIT"


def main():
    input_filename = "transcript.txt"
    # read the input file contents
    with open(input_filename, "r", encoding="utf-8") as input_file:
        transcript = input_file.read()

    # perform cleanup
    ## remove parts
    transcript = re.sub(r"^{[0-9]+}\s", "", transcript, 0, re.MULTILINE)

if __name__ == "__main__":
    main()
