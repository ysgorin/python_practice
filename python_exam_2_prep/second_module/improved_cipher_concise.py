# A concise version of improved_cipher.py.
# The code is from Codeium in response to my
# request to make improved_cipher.py more
# concise. Comments are my own.

# Set up a get_input function rather than a while
# loop for each user_input.
def get_input(prompt, validate_func, error_message):
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        else:
            print(error_message)

def validate_text(text):
    return text != ''

def validate_shift_value(shift_val):
    return shift_val.isdigit() and 1 <= int(shift_val) <= 25

txt = get_input('Enter a line of text for encryption: ',
                validate_text, 'You didn\'t enter any text for encryption.')
shift_val = get_input('Enter an encryption shift value between 1 and 25: ',
                      validate_shift_value, 'You didn\'t enter an integer between 1 and 25.')

cipher = ''
for char in txt:
    if char.isalpha():
        if char.islower():
            ascii_offset = ord('a')
        else:
            ascii_offset = ord('A')
        # Use modulo operator to find remainder
        # Remember 20 % 26 = 20, 27 % 26 = 1
        code = (ord(char) - ascii_offset + int(shift_val)) % 26 + ascii_offset
        cipher += chr(code)
    else:
        cipher += char

print('Cryptogram: ' + cipher)