# Function to evaluate Body Mass Index (BMI
# Weight (kg) / height (m)^2

# Convert imperial measurements to metric
# 1 lb = 0.45359237 kg
# 1 ft = 0.3048 m
# 1 in = 2.54 cm = 0.0254 m

def lb_to_kg(lb):
    return lb * 0.45359237

# Cannot name second parameter 'in' because
# 'in' is a Python keyword.
# Give 'inch' a default value of 0.0 for someone
# inputs feet with no inches
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

weight_input = \
float(input('What is your weight (lb)? '))

height_input = \
float(input('What is your height? (ft, in) '))

print(bmi(lb_to_kg(weight_input), ft_and_inch_to_m(height_input)))