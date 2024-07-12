# * You need a program to evalue the students'
#   average scores;
# * The program should ask for the student's name
#   followed by her/his single score;
# * The names ma be entered in any order;
# * Entering  am empty name finishes the
#   inputting of the data (note: entering an
#   empty score will raise the ValueError
#   exception).
# * A list of all names, together with the
#   evaluated average score should be outputted.

# Create an empty dictionary
school_class = {}

# Create a loop to add students and their scores.
while True:
    name = input("Enter the student's name: ")
    # exit the loop if an empty name is entered
    if name == '':
        break

    score = int(input("Enter the student's score\
 (0-10): "))
    
    # exit the loop if an out-of-range value is
    # entered
    if score not in range(0, 11):
        break

    # check if the student's name has already
    # been entered
    if name in school_class:
        # If true, add score to already existing
        # score tuple
        school_class[name] += (score,)
    # If false, add new key-value pair:
    # Student's name-score tuple
    else:
        school_class[name] = (score,)

# Loop through each student's (in alphabetical
# order) scores
for name in sorted(school_class.keys()):
    # Create a total score variable
    adding = 0
    # Create a number of scores variable
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)