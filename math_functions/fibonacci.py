# Fibonacci Numbers are a sequence of integer
# numbers built using a very simple rule:
# * the first element of the sequence is equal
#   to one (Fib1 = 1)
# * the second is also equal to one (Fib2 = 1)
# * every subsequent number is the sum of the two
#   preceding numbers:
#   Fib(i) = Fib(i-1) + Fib(i-2)

# For example:
#   fib_3 = 1 + 1 = 2
#   fib_4 = 1 + 2 = 3

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))
