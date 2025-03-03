# Each line of the file contains three elements: 
# the student's first name, the student's last 
# name, and the number of points the student 
# received during certain classes.
# The elements are separated with white spaces.
# Each student may appear more than once

# The file may look like this:
# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5

# Note:
# your program must be fully protected against
# all possible failures: the file's
# non-existence, the file's emptiness, or any
# input data failures; encountering any data
# error should cause immediate program
# termination, and the erroneous should be
# presented to the user;
# implement and use your own exceptions hierarchy
# - we've presented it in the editor; the second 
# exception should be raised when a bad line is 
# detected, and the third when the source file 
# exists but is empty.

from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

# ask the user for the file name
file_name = input('Enter file name: ')
data_dict = {}

try:
    file = open(file_name, 'rt')
    line = file.readline()
    while line != '':
        lst = line.split()
        if lst[0] + lst[1] in data_dict:
            data_dict[lst[0] + ' ' + lst[1]].append(float(lst[2]))
        else:
            data_dict[lst[0] + ' ' + lst[1]] = [float(lst[2])]
        line = file.readline()
    file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

print(data_dict)
# read the file contents and count the sum of the
# received points for each student

# print a simple but sorted report
# Expected output:
# Andrew Cox 	 1.5
# Anna Boleyn 	 15.5
# John Smith 	 7.0