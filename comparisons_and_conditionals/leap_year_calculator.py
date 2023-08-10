# Since the introduction of the Gregorian calendar (in 1582),
# the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

# The code should output one of two possible messages,
# which are 'Leap year' or 'Common year', depending on the value entered.

# It would be good to verify if the entered year falls into
# the Gregorian era, and output a warning otherwise:
# 'Not within the Gregorian calendar period'.

# Starter Code:
# year = int(input("Enter a year: "))
#
# Write your code here.
#	

year = int(input("Enter a year: "))

if year >= 1582:
    if year % 4 != 0:
        print('Common year')
    elif year % 100 != 0:
        print('Leap year')
    elif year % 400 != 0:
        print('Common year')
    else:
        print('Leap year')
else:
    print('Not within the Gregorian calendar period')
