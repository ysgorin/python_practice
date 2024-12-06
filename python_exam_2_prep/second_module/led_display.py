# LED Display

led_dict = {'0':['###',
                 '# #',
                 '# #',
                 '# #',
                 '###'],
            '1':['  #',
                 '  #',
                 '  #',
                 '  #',
                 '  #'],
            '2':['###',
                 '  #',
                 '###',
                 '#  ',
                 '###'],
            '3':['###',
                 '  #',
                 '###',
                 '  #',
                 '###'],
            '4':['# #',
                 '# #',
                 '###',
                 '  #',
                 '  #'],
            '5':['###',
                 '#  ',
                 '###',
                 '  #',
                 '###'],
            '6':['###',
                 '#  ',
                 '###',
                 '# #',
                 '###'],
            '7':['###',
                 '  #',
                 '  #',
                 '  #',
                 '  #'],
            '8':['###',
                 '# #',
                 '###',
                 '# #',
                 '###'],
            '9':['###',
                 '# #',
                 '###',
                 '  #',
                 '###']}

# Prompt user for number
prompt = False
while prompt == False:
    output = input('What non-negative integer number should the LED display show? ')
    # Only accept non-negative numbers
    if output.isdigit():
        break
    else:
        print('You must type a non-negative integer.')

# Process each line
for row in range(5):
    # Process each digit
    for i in range(len(output)):
        # use end='' to stay on the same line
        print(led_dict[output[i]][row], end='')
        # if it is not the last digit, add a space to separate between digits
        if i+1 != range(len(output)):
            print(' ', end='')
    # if it is not the fifth row, go to the next line
    if row != 4:
        print()