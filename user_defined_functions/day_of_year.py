# Your task is to write and test a function which
# takes three arguments (a year, a month, and a
# day of the month) and returns the corresponding
#  day of the year, or returns None if any of the
# arguments is invalid.

def is_year_leap(year):
    if(year % 4 != 0):
        return False
    elif(year % 100 != 0):
        return True
    elif(year % 400 != 0):
        return False
    else:
        return True

def day_of_year(year, month, day):
    month_lengths = {1: 31,
                     2: 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31}
    if is_year_leap(year) == True:
        month_lengths[2] = 29
    days = 0
    for i in range(1,month):
        days += month_lengths[i]
    days += day
    return days