# There once was a hat. The hat contained no
# rabbit, but a list of five numbers:
# 1, 2, 3, 4, 5.

# Your task is to:
# 1 Write a line of code that promopts the user
#   to replace the middle number in the list with
#   an integer number entered by the user.
# 2 Write a line of code that removes the last
#   element from the list.
# 3 Write a line of code that prints the length
#   of the existing list.

# Dependencies
import time

# Hat
hat = [1, 2, 3, 4, 5]
print('The hat contains the following list:', hat)
time.sleep(2)

# Prompt to replace the middle number in the list
# with an integer number
update_middle = int(input('Enter an integer to \
replace the middle number: '))
middle_index = len(hat) // 2
hat[middle_index] = update_middle
print('Now the hat contains this list:', hat)
time.sleep(2)

# Write a line of code that removes the last
# element from the list
del hat[-1]
print('As you can see the last number is gone:', hat)
time.sleep(2)

# Write a line of code that prints the length
# of the existing list
print('The length of the final list is:', len(hat))
