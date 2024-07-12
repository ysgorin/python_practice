# Function to evaluate Body Mass Index (BMI
# Weight (kg) / height (m)^2

def bmi(weight, height):
    return weight / height ** 2

weight_input = float(input('What is your weight (kg)? '))
height_input = float(input('What is your height? (m) '))

print(bmi(weight_input, height_input))
