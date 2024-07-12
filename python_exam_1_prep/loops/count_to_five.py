# Your task is very simple here:
#  write a program that uses a for loop to
# "count mississippily" to five.
# Having counted to five, the program should print to
# the screen the final message "Ready or not, here I come!"

# Starter Code
# import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

# Dependencies
import time

# Write a for loop that counts to five.
for count in range(1,6):
    # Body of the loop - print the loop iteration number
    # and the word "Mississippi".
    print(count, 'Mississippi')
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)
print('Ready or not, here I come!')
