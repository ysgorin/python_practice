# find_a_word.py

# Take two strings: one being a word and the
# second being a combination of any characters.
# Write a program that checks if the characters
# comprising the word are hidden inside the
# second string.

while True:
    word = input('Enter a word: ')
    if word.isalpha():
        break
    else:
        print('Invalid input. You must enter a word. Letters only.')

second_str = input('Enter a combination of characters: ')

for i in range(len(word)):
    if i == 0:
        if second_str.find(word[i]) != -1:
            continue
        else:
            print('No')
            break
    elif i == len(word) - 1:
        if second_str.find(word[i], word.index(word[i-1])) != -1:
            print('Yes')
        else:
            print('No')
            break
    else:
        if second_str.find(word[i], word.index(word[i-1])) != -1:
            continue
        else:
            print('No')
            break