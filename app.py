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

print(openOrSenior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))