# char_freq_histo.py

# Character Frequency Histogram

# Expected output based on test_file.txt:
# a -> 1
# b -> 1
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
            histo_dict[ch.lower()] = 1
        ch = s.read(1)
    s.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
except:
    print('A non-I/O error occured')

# prints a simple histogram in alphabetical
# order (only non-zero counts should be
# presented)
for k, v in histo_dict.items():
    print(k, '->', v)