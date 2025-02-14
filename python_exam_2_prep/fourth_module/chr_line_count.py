# Use to diagnose stream problems
from os import strerror

try:
    # create two variables both equal to 0
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    # read first line and advance virtual head to end of line
    line = s.readline()
    # after all lines are read, readline() will return an empty string
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        # read next line
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))