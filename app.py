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
    masked = string
    for idx, c in enumerate(string):
        if idx < len(string) - 4:
            print(idx, c)
            masked.replace('1', "#")
   
    print(masked)
    # return string if len(string) < 5 else string.replace('*', "#"[len(string) - 4])


print(maskify('123456'))