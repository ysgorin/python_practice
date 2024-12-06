# anagrams.py

# An anagram is a new word formed by rearranging
# the letters of a word, using all the original
# letters exactly once.

# Write a program that asks the user for two
# separate texts, checks whether the entered
# texts are anagrams, and prints the result.

# Test Data
# Sample Input:
#    'Listen'
#    'Silent'
# Sample Output:
#    'Anagrams'

# Sample Input:
#    'modern'
#    'norman'
# Sample Output:
#    'Not anagrams'

# Dependencies
from time import sleep

def anagram_check(word_1, word_2):
    if len(word_1) != 0:
        # Treat upper- and lower-case letters as equal
        # Spaces are not taken into account during the check
        word_1, word_2 = word_1.replace(' ','').lower(), word_2.replace(' ','').lower()
        return sorted(list(word_1)) == sorted(list(word_2))
    # Assume that two empty strings are not anagrams
    else:
        return False
    
print('*** Anagram Test ***')
sleep(1)

while True:
    word_1, word_2 = input('Enter the first text: '), input('Enter the second text: ')
    if anagram_check(word_1,word_2):
        print('Anagrams')
    else:
        print('Not anagrams')
    
    sleep(1)
    cont = input('Test other words? (Enter \'y\' or \'n\') ')
    if cont == 'n':
        break