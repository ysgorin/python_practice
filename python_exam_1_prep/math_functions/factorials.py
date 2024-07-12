# Factorials

# 0! = 1 
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 ... * n-1 * n

# Marked with an exclamation point and is equal
# to the product of all natural numbers from one
# up to its argument.

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

for n in range(1, 6):
    print(n, factorial_function(n))