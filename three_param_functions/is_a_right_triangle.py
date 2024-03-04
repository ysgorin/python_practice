def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    else:
        b ** 2 == a ** 2 + c ** 2

print('Follow the prompts to check if your three\
 side lengths make a right triangle.')

a = float(input('Enter the first side\'s length:\
 '))

b = float(input('Enter the second side\'s\
length: '))

c = float(input('Enter the third side\'s length:\
 '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a right triangle.')
else:
    print('No, it can\'t be a right triangle.')