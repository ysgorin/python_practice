# Function to evaluate Body Mass Index (BMI
# Weight (kg) / height (m)^2

def bmi(weight, height):
    # Add condition to return 'None' if input
    # values don't make sense.
    # Use the backslash (\) charcter to avoid
    # long lines of code.
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

weight_input = \
float(input('What is your weight (kg)? '))

height_input = \
float(input('What is your height? (m) '))

print(bmi(weight_input, height_input))