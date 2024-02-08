# Your task is to write and test a function which
# takes two arguments (a year and a month) and
# returns the number of days for the given
# month/year pair (while only February is
# sensitive to the year value, your function
# should be universal).

# Function to determine if year is leap year
def is_year_leap(year):
    if(year % 4 != 0):
        return False
    elif(year % 100 != 0):
        return True
    elif(year % 400 != 0):
        return False
    else:
        return True
    
# Function to determine days in a month/year pair
def days_in_month(year, month):
    month_lengths = {1: 31,
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
    if month == 2 and is_year_leap(year) == False:
        return 28
    elif month == 2 and is_year_leap(year) == True:
        return 29
    else:
        return month_lengths[month]

# Testing code
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
