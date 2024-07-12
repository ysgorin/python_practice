# Miles and kilometers are units of length or distance.
# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers,
# complete the program in the editor so that it converts:
# * miles to kilometers;
# * kilometers to miles.

# Starter Code:
# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = ###
# kilometers_to_miles = ###

# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")