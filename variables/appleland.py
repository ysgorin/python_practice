# Here is a short story:
# Once upon a time in Appleland, John had three apples, Mary had five apples,
# and Adam had six apples. They were all very happy and lived for a long time.
# End of story.

# Your task is to:
# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
# now create a new variable named total_apples equal to addition of the three former variables.
# print the value stored in total_apples to the console;

john, mary, adam = 3, 5, 6
print("John has",john,"apples, Mary has",mary,"apples, and Adam has",adam,"apples.")
total_apples = john + mary + adam
print("Together they have",total_apples,"apples.")