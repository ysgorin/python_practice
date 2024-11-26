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

def get_input(prompt, validate_func, error_message):
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        else:
            print(error_message)

def validate_month(month):
    if month.isdigit():
        return 1 <= int(month) <= 12
    else:
        return False

def validate_day(day):
    if day.isdigt():
        return
    else:
        return False
        

def validate_year(year):
    if year.isdigit():
        return
    else:
        return False


print('*** The Digit of Life ***')
sleep(1)
while True:
    birthdate = input('Enter your birthdate (YYYYMMDD, YYYYDDMM, MMDDYYYY): ')
    if birthdate.isdigit():
        break
    else:
        print('Invalid input. Enter digits only. ')
        sleep(1)