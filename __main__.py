#!/usr/bin/env python3

import re

__author__ = "Eryk Darnowski"
__version__ = "0.0.0"
__license__ = "MIT"


def main():
    input_filename = "transcript.txt"
    regex_patterns = [
            "http(s)?:\/\/",
            "(Przekazano wiadomość|przekazuje wiadomość)",
            "(C|c)ofn(ięto|ęła)\swys(y)?łanie\swiadomości",
            "Załącznik niedostępnyTen załącznik mógł zostać usunięty lub",
            "(Odpowiedziałeś(aś)\s|Oryginalna wiadomość:|Użytkownik  odpisał Ci|odpowiedział)",
            "^(|\s+)$",
        ]

    # read the input file contents
    with open(input_filename, "r", encoding="utf-8") as input_file:
        transcript = input_file.read()

    # perform cleanup
    ## remove parts
    transcript = re.sub(r"^{[0-9]+}\s", "", transcript, 0, re.MULTILINE)

    ## remove lines
    transcript = transcript.splitlines()
    transcript = [line for line in transcript if not any(re.search(pattern, line) for pattern in regex_patterns)]
    print(transcript)


if __name__ == "__main__":
    main()
