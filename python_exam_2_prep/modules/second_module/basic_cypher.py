# Caesar cipher.
text = input("Enter your message: ")

# Use all caps
text = text.upper()
print(text)

# cipher variable
cipher = ''

for char in text:
    if not char.isalpha():
        cipher += ' '
        continue
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)