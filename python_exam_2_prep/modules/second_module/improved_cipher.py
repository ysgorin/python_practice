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