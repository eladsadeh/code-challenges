'''
 Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
'''

def wordSpin(sentence):
    spinned = []
    for word in sentence.split():
        if len(word) > 4:
            word = word[::-1]

        spinned.append(word)

    return ' '.join(spinned)

# solution from codewars
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# wordSpin('This is another test')

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(string):
    return (len(string)-4) * '#' + string[-4:]

# print(maskify(''))

# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    output = []
    for person in data:
        output.append("Senior" if person[0] >=55 and person[1] > 7 else "Open")

    return output

# Solution from codewars
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# print(openOrSenior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

# Simple: given a string of words, return the length of the shortest word(s). String will never be empty, and you do not need to account for different data types.

def shortest_word(string):
    return min([len(w) for w in string.split()])

print(shortest_word("It don't think that word means what you think it means"))

def sum_of_minimums(list):
    return sum([min(l) for l in list])

my_list = [
    [7,8,3,4,5], # minimum value of row is 1
    [11, 15,20,6,7,8,9], # minimum value of row is 5
    [100, 40,21,34,56] # minimum value of row is 20
    ]

# print(sum_of_minimums(my_list))

def split_strings(s):
    print([s[i:i+2] if i+2 <= len(s) else s[i] + '_' for i in range(0, len(s), 2) ])

# from codewars
# import re

# def solution(s):
#     return re.findall(".{2}", s + "_")
   
    

print(split_strings('xyaappldldo'))
# should return ['ab', 'c_']



print(split_strings('abcdef'))
# should return ['ab', 'cd', 'ef']