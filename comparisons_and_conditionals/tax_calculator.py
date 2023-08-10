# Evaluate tax using the following rule:

# if the citizen's income was not higher
# than 85,528 thalers, the tax was equal to 18%
# of the income minus 556 thalers and 2 cents
# (this was the so-called tax relief)

# if the income was higher than this amount,
# the tax was equal to 14,839 thalers and 2 cents,
# plus 32% of the surplus over 85,528 thalers.

# Write a tax calculator
# It should accept one floating-point value: the income.
# it should print the calculated tax, rounded to full thalers.

# Note: this happy country never returns money to its citizens.
# If the calculated tax is less than zero,
# it only means no tax at all (the tax is equal to zero).

# Starter Code
# income = float(input("Enter the annual income: "))
# Write your code here.
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * .18 - 556.2
    if tax < 0:
        tax = 0.0
else:
    tax = 14839.2 + (income - 85528) * .32

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
