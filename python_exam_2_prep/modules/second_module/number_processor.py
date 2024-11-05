# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    if len(strings) == 0:
        print("The total is:", total)
    else:
        print('You didn\'t enter any numbers.')
except:
    print(substr, "is not a number.")
