# Scenario
# The Beatles were one of the most popular music
# group of the 1960s, and the best-selling band
# in history. Some people consider them to be the
#  most influential act of the rock era. Indeed,
# they were included in Time magazine's
# compilation of the 20th Century's 100 most
# influential people.

# The band underwent many line-up changes,
# culminating in 1962 with the line-up of
# John Lennon, Paul McCartney, George Harrison,
# and Richard Starkey (better known as Ringo
# Starr).

# Write a program that reflects these changes and
# lets you practice with the concept of lists.
# Your task is to:

# step 5: use the insert() method to add Ringo
# Starr to the beginning of the list.

# Dependencies
import time

# step 1: create an empty list named beatles;
# step 1
beatles = []
print("Step 1:", beatles)
time.sleep(1)

# step 2: use the append() method to add the
# following members of the band to the list:
# John Lennon, Paul McCartney, and George
# Harrison;
# step 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 2:", beatles)
time.sleep(1)

# step 3: use the for loop and the append()
# method to prompt the user to add the following
# members of the band to the list: Stu Sutcliffe,
# and Pete Best;
# step 3
user_input = [input('Type \'Stu Sutcliffe\' to add him to the band. '), input('Type \'Pete Best\' to add him to the band. ')]
for input in user_input:
    beatles.append(input)
print("Step 3:", beatles)
time.sleep(1)

# step 4: use the del instruction to remove Stu
# Sutcliffe and Pete Best from the list;
# step 4
del beatles[3:5]
print("Step 4:", beatles)
time.sleep(1)

# step 5: use the insert() method to add Ringo
# Starr to the beginning of the list.
# step 5
beatles.insert(0, 'Ringo Starr')
print("Step 5:", beatles)
time.sleep(1)

# testing list length
print("The Fab", len(beatles))