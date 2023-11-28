"""
Better checker than Arthur's
"""

from collections import Counter

ANSWER_FILE = "answer_file_here"

with open(ANSWER_FILE, "r") as fhand:
    line = fhand.readline()
    t = line.split("),")[:-1]
    print(Counter([s.split(",")[1][1:] for s in t]))