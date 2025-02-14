# import strerror for diagnosising stream problems
from os import strerror

try:
    cnt = 0
    s = open('text.txt', 'r')
    ch = s.read(1) # read one character of the stream
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1) # read next character
    s.close()
    print('\n\nCharacters in file: ', cnt)
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))