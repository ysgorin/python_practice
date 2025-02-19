from os import strerror

try:
    ccnt = lcnt = 0
	# The object returned by the open() function
    # is an instance of the iterable class.
    for line in open('text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    # Expected behavior is that the iterable
    # automatically invokes close() when the end
    # of the file is reached.
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))