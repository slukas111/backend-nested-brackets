#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Sasha Lukas w/ help Chris"

import sys

def is_matched(s):
    brac_types = {
        "parasts": ["(*", "*)"],
        "parens": ["(", ")"],
        "brackets": ["[", "]"],
        "curlies": ["{", "}"],
        "inequalities": ["<", ">"]
    }

    opn_bracket = []
    index = 0
    answer = "Yes"
    while s:
        index += 1
        if s[:2] == "(*" or s[:2] == "*)":
            token = s[:2]
 else:
            token = s[0]
        for bracket_maybe in brac_types:
            if token == brac_types[bracket_maybe][0]:
                opn_bracket.append(token)
            if token == brac_types[bracket_maybe][-1]:
                if opn_bracket[-1] != brac_types[bracket_maybe][0]:
                    answer = "NO " + str(index)
                    #pass
                    token = s
                else:
                    opn_bracket.pop()
        s = s[len(token):]
    if len(opn_bracket) > 0:
        answer = "NO " + str(index)
    return answer
    
def is_nested(line):
    """Validate a single input line for correct nesting"""
    pass


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
