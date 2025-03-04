# Write a function or method called find that 
# takes two arguments called path and dir. The 
# path argument should accept a relative or 
# absolute path to a directory where the search 
# should start, while the dir argument should be 
# the name of a directory that you want to find 
# in the given path. Your program should display 
# the absolute paths if it finds a directory with
# the given name.

# The directory search should be done
# recursively. This means that the search should 
# also include all subdirectories in the given path.

# Import os module
import os

def find(path, dir_name):
    paths = [] # empty list to store results

    for root, dirs, files in os.walk(path):
        if dir_name in dirs:
            paths.append(os.path.join(root , dir_name))
    
    if paths:
        for path in paths:
            print(path)

    else:
        print(f'No directory named \'{dir_name}\' found in {path}.')

find(input('enter path: '), input('enter dir_name: '))