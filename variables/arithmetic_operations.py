# Take a look at the code in the editor:
# it reads a float value,
# puts it into a variable named x,
# and prints the value of a variable named y.
# Your task is to complete the code in order to evaluate the following expression:
# The expression is found in ../screenshots/artihmetic.operations.png
# The result should be assigned to y.

# Starter Code:
# x =  # hardcode your test data here
# x = float(x)
# # write your code here
# print("y =", y)

x =  float(input('Enter a number: '))
y = (3 * x**3) - (2 * x**2) + (3 * x) - 1
print("y =", y)