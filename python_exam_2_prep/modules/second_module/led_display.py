# Every digit is five lines of three characters.
# The middle character on the second and fourth lines
# is always a space.
# So, I think a nested list is in order here.
# Also there should be a space between each digit.

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
    if output.isdigit():
        break

for row in range(5):
    for i in range(len(output)):
        print(led_dict[output[i]][row], end='')
        if i+1 != range(len(output)):
            print(' ', end='')
    if row != 4:
        print()