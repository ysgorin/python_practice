# Every digit is five lines of three characters.
# The middle character on the second and fourth lines
# is always a space.
# So, I think a nested list is in order here.
# Also there should be a space between each digit.

led_dict = {0:{1:'###',
               2:'# #',
               3:'# #',
               4:'# #',
               5:'###'},
            1:{1:'  #',
               2:'  #',
               3:'  #',
               4:'  #',
               5:'  #'},
            2:{1:'###',
               2:'  #',
               3:'###',
               4:'#  ',
               5:'###'},
            3:{1:'###',
               2:'  #',
               3:'###',
               4:'  #',
               5:'###'},
            4:{1:'# #',
               2:'# #',
               3:'###',
               4:'  #',
               5:'  #'},
            5:{1:'###',
               2:'#  ',
               3:'###',
               4:'  #',
               5:'###'},
            6:{1:'###',
               2:'#  ',
               3:'###',
               4:'# #',
               5:'###'},
            7:{1:'###',
               2:'  #',
               3:'  #',
               4:'  #',
               5:'  #'},
            8:{1:'###',
               2:'# #',
               3:'###',
               4:'# #',
               5:'###'},
            9:{1:'###',
               2:'# #',
               3:'###',
               4:'  #',
               5:'###'}}

# Prompt user for number
prompt = False
while prompt == False:
    output = input('What non-negative integer number should the LED display show? ')
    if output.isdigit():
        break

digits = list(output)
for row in range(5):
    for i in range(len(digits)):
        print(led_dict[int(digits[i])][row + 1], end='')
        if i+1 != len(digits):
            print(' ', end='')
    if row+1 != 5:
        print()