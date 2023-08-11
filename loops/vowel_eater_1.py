# The continue statement is used to skip the current block and move
# ahead to the next iteration, without executing the statements inside the
# loop.

# It can be used with both the while and for loops.

# Your task here is very special: you must design a vowel eater! Write a
# program that uses:

# * a for loop;
# * the concept of conditional execution (if-elif-else)
# * the continue statement.

# Your program must:
# * ask the user to enter a word;
# * use user_word = user_word.upper() to convert the word
#   entered by the user to upper case; we'll talk about the
#   so-called string methods and the upper() method very soon - don't worry;
# * use conditional execution and the continue statement to "eat" the
#   following vowels A, E, I, O, U from the inputted word;
# * print the uneaten letters to the screen, each one of them on a
#   separate line.

word = input('Enter a word: ')
word = word.upper()
for letter in word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter)
