#!/usr/bin/env python3

import re
import json

__author__ = "Eryk Darnowski"
__version__ = "0.0.0"
__license__ = "MIT"


def is_sender(string):
    return string[0] == " "

def main():
    input_filename = "transcript.txt"
    output_filename = "output.jsonl"
    config = {
        "role": "system",
        "content": "Jestem Marek, chat bot bazowany na wiadomościach z Messengera, który ma na celu imitować chat z tą osobą.",
    }
    regex_patterns = [
            "http(s)?:\/\/",
            "(Przekazano wiadomość|przekazuje wiadomość)",
            "(C|c)ofn(ięto|ęła)\swys(y)?łanie\swiadomości",
            "Załącznik niedostępnyTen załącznik mógł zostać usunięty lub",
            "(Odpowiedziałeś\(aś\)\s|Oryginalna wiadomość:|Użytkownik  odpisał Ci|odpowiedział)",
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


    # split by sender / receiver + format
    convo_list = [];
    convo = { "messages": [ config ] }

    # go through each line
    for i in range(len(transcript) - 1):
        curr_is_sender = is_sender(transcript[i])

        # needs to be first to keep the: prompts first, answers later schema
        if curr_is_sender:
            convo["messages"].append({ "role": "user", "content": transcript[i].lstrip() })
        else:
            if (len(convo["messages"]) > 1):
                convo["messages"].append({ "role": "assistant", "content": transcript[i] })

        # making sure that the convo won't start with an answer to a non existant prompt
        if (not curr_is_sender and is_sender(transcript[i + 1])):
            if (len(convo["messages"]) > 1):
                convo_list.append(convo)
            convo = { "messages": [ config ] }


    # write output
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for convo in convo_list:
            json.dump(convo, output_file, ensure_ascii=False)
            output_file.write('\n')


if __name__ == "__main__":
    main()
