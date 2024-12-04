# read_ints.py

# Write a function able to input intger values
# and to check if they are within a specified
# range.

def read_int(prompt, min, max):
    while True:
        try:
            v = int(input(prompt))
            if min <= v <= max:
                return v
            else:
                raise Exception
        except ValueError:
            print('Error: wrong input')
        except:
            print(f'Error: the value is not within the permitted range ({min}..{max})')

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)