# palindrome.py

# Check if a user input is a palindrome.

# Test data
# Sample input: Ten animals I slam in a net
# Sample output: It's a palindrome
# Sample input: Eleven animals I slam in a net
# Sample output: It's not a palindrome

from time import sleep
print('** Palindrome Test **')
sleep(1)

while True:
    user_input = input('Enter a string: ')
    # spaces are not taken into account
    # treat upper- and lower-case letters as equal
    word = user_input.replace(' ','').lower()
    # An empty string is not a palindrome
    if len(word) != 0:
        palindrome = True
        for i in range(len(word) // 2):
            if word[i] == word[-(i+1)]:
                continue
            else:
                palindrome = False
        if palindrome:
            print('It\'s a palindrome.')
        else:
            print('It\'s not a palindrome.')
    else:
        print('It\'s not a palindrome.')
    sleep(1)
    cont = input('Test another word? (Enter \'y\' or \'n\') ')
    if cont == 'n':
        break