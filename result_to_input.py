"""
Script that outputs steps with double quotation marks around coordinate to be put in grid4.py/grid8.py
"""
ANSWER_FILE = "answer_file_here"

with open(ANSWER_FILE, "r") as fhand:
    line = fhand.readline()
    print("),".join([s[:-2] + "\"" + s[-2:] + "\"" for s in line.split("),")[:-1]]) + ")")