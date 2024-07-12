# Vowel Eater 3

# A more concise version of vowel eater 2

word = input('Enter a word: ')
word = word.upper()

for letter in word:
    if letter in ('A','E','I','O','U'):
        continue
    else:
        print(letter, end='')
