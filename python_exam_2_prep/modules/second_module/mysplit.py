# Your task is to write your own function, which
# behaves almost exactly like the original split() method, i.e.:
# it should accept exactly one argument - a string;
# it should return a list of words created from the string,
#   divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()

def mysplit(string):
    word_list = []
    word = ''
    for chr in string:
        if chr.isspace() == False:
            word = word + chr
        else:
            if word.isalnum():
                word_list.append(word)
            word = ''
    if word.isalnum():
        word_list.append(word)
    return word_list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))