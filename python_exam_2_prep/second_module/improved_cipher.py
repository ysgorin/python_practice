# The original Caesar cipher shifts each
# character by one: a becomes b, z becomes a,
# and so on. Let's make it a bit harder and allow
# the shifted value to come from the range 1..25
# inclusive.
# Let the code preserve the letter's case and all
# non-alphabetical characters should remain untouched.
# Your task is to write a program which:
# * asks the user for one line of text to encrypt
# * asks the user for a shift value (an integer
# number from the range 1..25 - note: you should
# force the user to enter a valid shift value)
# prints out the encoded text

# Sample input:
# 'abcxyzABCxyz 123'
# 2
# Sample output: 
# 'cdezabCDEzab 123'

# Control variable
txt_ctrl = False
while txt_ctrl == False:
    txt = input("Enter a line of text for encryption: ")
    if txt == '':
        print('You didn\'t enter any text for encryption.')
    else:
        txt_ctrl = True

shift_val_ctrl  = False
while shift_val_ctrl == False:
    shift_val = input("Enter an encryption shift value between 1 and 25: ")
    if not shift_val.isdigit():
        print('You didn\'t enter an integer between 1 and 25.')
    elif int(shift_val) < 1 or int(shift_val) > 25:
        print('You didn\'t enter an integer between 1 and 25.')
    else:
        shift_val_ctrl = True

# Cipher variable
cipher = ''

# Iterate through text
for char in txt:
    code = ord(char) + int(shift_val)
    if not char.isalpha():
        cipher += char
    elif char.islower():
        if code <= ord('z'):
            cipher += chr(code)
        elif code > ord('z'):
            code = (ord('a') + (int(shift_val) - (ord('z') - ord(char)))) - 1
            cipher += chr(code)
    elif char.isupper():
        if code <= ord('Z'):
            cipher += chr(code)
        elif code > ord('Z'):
            code = (ord('A') + (int(shift_val) -(ord('Z') - ord(char)))) - 1
            cipher += chr(code)
print('Cryptogram: ' + cipher)