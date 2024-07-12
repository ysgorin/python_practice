# Your task is to prepare a simple code able to
# evaluate the end time of a period of time,
# given as a number of minutes (it could be arbitrarily large).
# The start time is given as a pair of hours (0..23) and minutes (0..59).
# The result has to be printed to the console.

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Starter Code:
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# find a total of all minutes
# find a number of hours hidden in minutes and update the hour
# correct minutes to fall in the (0..59) range
# correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# find a total of all minutes
total_mins = mins + dura
# find a number of hours hidden in minutes and update the hour
hours_to_add = total_mins // 60
# correct minutes to fall in the (0..59) range
mins = total_mins - (hours_to_add * 60)
# correct hours to fall in the (0..23) range
hour = (hour + hours_to_add) % 24

print(hour, ":", mins, sep='')