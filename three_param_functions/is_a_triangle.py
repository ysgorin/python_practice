# A function to check whether three sides of
# given lengths can build a triangle.

# The sum of two arbitrary sides has to be longer
# than the third side.

# If the sides can be a triangle, return True
# If not, return False

# Check to see if the sum of any two sides is
# less than the third.

# Version 1
# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True

# Version 2 - More Compact
# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True

# Version 3 - Even more compact
# If all conditions are true, then return true.
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))