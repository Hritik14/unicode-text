#!/bin/python
import random

CONFUSABLES = "./unicode.txt"
string = input()
m = {}
with open(CONFUSABLES, "r") as f:
    txt = f.read().split("\n")
    for line in txt:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        tokens = line.split(";")
        if len(tokens) < 2:
            continue

        key = "".join([chr(int(t, 16)) for t in tokens[1].split()])
        val = chr(int(tokens[0], 16))

        if key in m:
            m[key].append(val)
        else:
            m[key] = []

for c in string:
    try:
        print(random.choice(m[c]), end="")
    except KeyError:
        print(c, end="")
