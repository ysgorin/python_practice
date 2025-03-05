# Import os module
import os

# Write a function or method called find that
# takes two arguments called path and dir.
def find(path, dir):
    paths = [] # empty list to store results

    # Use os.walk to generate file names in a
    # directory tree
    # This will include all subdirectories for a
    # recursive search.
    for root, dirs, files in os.walk(path):
        if dir in dirs:
            # Join one or more path segments
            # intelligently
            # This will return absolute paths
            paths.append(os.path.join(root, dir))
    
    if paths:
        for path in paths:
            print(path)

    else:
        print(f'No directory named \'{dir}\' \
found in {path}.')

# The path argument should accept a relative or 
# absolute path to a directory where the search 
# should start, while the dir argument should be 
# the name of a directory that you want to find 
# in the given path.
find(input('Enter the relative or absolute path \
where your search should start: '), \
input('Enter the name of the \
directory that you want to \
find: '))


# See documentation here:
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/os.path.html