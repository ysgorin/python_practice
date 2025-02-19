from os import strerror

try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n" # Note: the newline is added
		# Version 1
		# The following loops through the string
		# and writes one character at a time.
		# for ch in s:
		# 	fo.write(ch)

		# Version 2
		# The following writes the entire string
		fo.write(s)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))