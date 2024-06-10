# The following code will raise an error if a
# non-integer or nothing is inputted.
# value = int(input('Enter a natural number: '))
# print('The reciprocal of', value, 'is', 1/value)

# A try-except branch can handle the error.
# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except:
#     print('I don't know what to do.')

# With the above, all errors will be handled equally.
# The following distinguishes between errors.
# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except ValueError:
#     print('I don\'t know what to do.')
# except ZeroDivisionError:
#     print('Division by zero is not allowed in our Universe.')


# While all exceptions are covered in the above code,
# this code has a default except branch as well.
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I don\'t know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')
