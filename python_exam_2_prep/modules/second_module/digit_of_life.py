# digit_of_life.py

# Some say that the Digit of Life is a digit
# evaluated using somebody's birthday. It's
# simple - you just need to sum all the digits of
# the date. If the result contains more than one
# digit, you have to repeat the addition until
# you get exactly one digit.

# Test Data
# Sample Input: '19991229'
# Sample Output: '6'

# Sample Input: '20000101'
# Sample Output: '4'

from time import sleep

print('*** The Digit of Life ***')
sleep(1)
while True:
    birthdate = input('Enter your birthdate (YYYYMMDD, YYYYDDMM, MMDDYYYY): ')
    if birthdate.isdigit():
        break
    else:
        print('Invalid input. Enter digits only. ')
        sleep(1)