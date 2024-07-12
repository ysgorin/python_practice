# Your task is to complete the code in order to evaluate the following expression.
# The result should be assigned to 'y'.
# The expression is found in ../screenshots/arithmetic_operations2.png

# Starter Code:
# x = float(input("Enter value for x: "))
# # Write your code here.
# print("y =", y)

x = float(input("Enter value for x: "))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y =", y)