# Caesar cipher.
text = input("Enter your message: ")

# Use all caps
text = text.upper()
print('Original Message: ' + text)

# cipher variable
cipher = ''

# iterate through text
for char in text:
    # skip if it is a non-Latin letter character
    if not char.isalpha():
        cipher += ' '
        continue
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print('Cryptogram: ' + cipher)