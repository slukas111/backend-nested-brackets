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


def is_nested(line):
    """Validate a single input line for correct nesting"""
    pass


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
