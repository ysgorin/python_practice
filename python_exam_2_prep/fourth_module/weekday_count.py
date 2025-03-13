# weekday_count.py

# Scenario
# During this course, we looked at the Calendar
# class a bit. Your task is to extend its
# functionality with a new method called
# count_weekday_in_year, which takes a year and a
# weekday as parameters, and then returns the
# number of occurrences of a specific weekday in
# the year.

# Use the following tips:

# Create a class called MyCalendar that extends
# the Calendar class;

import calendar

class MyCalendar(calendar.Calendar):

# create the count_weekday_in_year method with
# the year and weekday parameters. The weekday
# parameter should be a value between 0-6, where
# 0 is Monday and 6 is Sunday. The method should
# return the number of days as an integer;
    def count_weekday_in_year(self, year, weekday):
        weekday_count = 0
        for month in range(1,13):
            for i in self.monthdays2calendar(year, month):
                if i[weekday][0] != 0:
                    weekday_count += 1
        return weekday_count

# in your implementation, use the
# monthdays2calendar method of the Calendar class.

# The following are the expected results:
# Sample arguments
# year=2019, weekday=0
# Expected output
# 52

# Sample arguments
# year=2000, weekday=6
# Expected output
# 53

c = MyCalendar()

year = int(input('Enter a year: '))
weekday = int(input('Enter a weekday integer (0-6): '))

print(c.count_weekday_in_year(year, weekday))