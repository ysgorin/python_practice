# Find the area of a triangle using Heron's
# formula.

# Heron's formula finds the area of a triangle in
# terms of the lengths of its sides.

# If a, b, and c are the lengths of the sides,
# where 's' is half of the perimeter or
# (a + b + c)/2, area = square root of
# s(s-a)(s-b)(s-c)

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    # h_p = half of the perimeter
    h_p = (a + b + c) / 2
    # Use exponent 0.5 for square root
    return (h_p * (h_p - a) * (h_p - b) * \
            (h_p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print('Follow the prompts to check the area of\
 your triangle.')

a = float(input('Enter the first side\'s length:\
 '))

b = float(input('Enter the second side\'s\
length: '))

c = float(input('Enter the third side\'s length:\
 '))

print(area_of_triangle(a, b, c))