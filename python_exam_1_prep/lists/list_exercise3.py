# Your task is to write a program which removes
# all the number repetitions from the list.
# The goal is to have a list in which all the
# numbers appear not more than once.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for item in my_list:
    if item not in new_list:
        new_list.append(item)

new_list.sort()
my_list = new_list

print("The list with unique elements only:")
print(my_list)