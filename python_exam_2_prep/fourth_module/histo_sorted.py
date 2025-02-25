# histo_sorted.py

# Sorted character frequency histogram

# Expected output based on test_file.txt:
# a -> 3
# b -> 2
# c -> 1

from os import strerror

# ask the user for the input file's name 
file_name = input('Enter file name: ')
histo_dict = {}

try:
    # read the file and count all the Latin
    # letters (lower- and upper-case letters are
    # treated as equal)
    s = open(file_name, 'r')
    ch = s.read(1)
    while ch != '':
        # if it is a Latin character
        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            if ch.lower() in histo_dict:
                histo_dict[ch.lower()] += 1
            else:
                histo_dict[ch.lower()] = 1
        ch = s.read(1)
    s.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
except:
    print('A non-I/O error occured')

# the output histogram should be sorted based on
# the characters' frequency (the bigger counter
# should be presented first)
for k, v in sorted(histo_dict.items()):
    if v > 0:
        print(k, '->', v)

# the histogram should be sent to a file with the
# same name as the input one, but with the suffix
# '.hist' (it should be concatenated to the
# original name)