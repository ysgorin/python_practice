# read_ints.py

# Write a function able to input integer values
# and to check if they are within a specified
# range.

# Handle bad inputs using errors handling only
# for purposes of becoming familiar with
# exceptions.

def read_int(prompt, min, max):
    while True:
        try:
            v = int(input(prompt))
            assert min <= v <= max
            return v
        except ValueError:
            print('Error: wrong input')
        except AssertionError:
            print(f'Error: the value is not within the permitted range ({min}..{max})')

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)