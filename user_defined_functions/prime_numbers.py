# Scenario
# A natural number is prime if it is greater than
# 1 and has no divisors other than 1 and itself.

# Your task is to write a function checking
# whether a number is prime or not.

# The function:

# * is called is_prime;
# * takes one argument (the value to check)
# * returns True if the argument is a prime number,
#   and False otherwise.

# Hint: try to divide the argument by all
# subsequent values (starting from 2) and check
# the remainder - if it's zero, your number
# cannot be a prime; think carefully about when
# you should stop the process.

# If you need to know the square root of any
# value, you can utilize the ** operator.
# Remember: the square root of x is the same as
# x0.5

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
           return False
    else:
        return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
