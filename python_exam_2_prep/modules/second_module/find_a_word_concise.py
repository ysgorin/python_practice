# find_a_word_concise.py
# See find_a_word.py

# This version is the output of Codeium when
# asked to make find_a_word.py more concise.

def find_word():
    while True:
        word = input('Enter a word: ')
        if word.isalpha():
            break
        print('Invalid input. You must enter a word. Letters only.')

    second_str = input('Enter a combination of characters: ')
    index = 0

    for char in word:
        # Save the index position of the find for
        # the next iteration
        index = second_str.find(char, index)
        if index == -1:
            print('No')
            return

    print('Yes')

find_word()