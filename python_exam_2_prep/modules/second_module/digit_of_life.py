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
    if birthdate.isdigit() and len(birthdate) == 8:
        break
    else:
        print('Invalid input. Enter eight digits only. ')
        sleep(1)

digit_of_life = birthdate

while True:
    sum = 0
    for char in digit_of_life:
        sum += int(char)
    digit_of_life = str(sum)
    if len(digit_of_life) > 1:
        continue
    else:
        print(f'Your digit of life is: {str(sum)}.')
        break