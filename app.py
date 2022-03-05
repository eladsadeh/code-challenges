'''
 Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
'''

import enum


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

# print(shortest_word("It don't think that word means what you think it means"))

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
   
# print(split_strings('xyaappldldo'))
# # should return ['ab', 'c_']
# print(split_strings('abcdef'))
# should return ['ab', 'cd', 'ef']

# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def print_middle(word):
    print(len(word))
    print(int((len(word)-1)/2))

    print(word[(len(word)-1)/2] if (len(word)-1)%2 == 0 else word[(len(word)-2)/2])

# print_middle('abc')

# removes the first and last character of a string.
def remove_char(s):
    return s[1:-1]

# print(remove_char('eloquent')) # -> 'loquen'

# Find the greatest common divisor of two positive integers without using a Python library.

# def mygcd(x,y):
#     d = int(max(x,y,2)/2)
#     while d:
#         if x % d == 0 and  y% d == 0:
#             return int(d)
#         d -= 1

def mygcd(x,y):
    while y:
        x, y = y, x%y
    return x

# print(mygcd(30,1))
# print(mygcd(15713250,10063368))

# Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

def highest(s):
    alfa = '0abcdefghijklmnopqrstuvwxyz'
    high_score = 0
    for word in s.split():
        score = sum([alfa.index(c) for c in word])
        if score > high_score:
            high_score = score
            high_word = word
    return high_word

# Codewars solution
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# print(highest('man i need a taxi up to ubud')) # -> 'taxi'
# print(highest('what time are we climbing up the volcano')) # -> 'volcano'
# print(highest('take me to semynak')) # -> 'semynak'

def diagonalDifference(arr):
    for idx, row in enumerate(arr): print(idx, row)
    diag1 = 0
    diag2 = 0
    for i in range(len(arr)):
        diag1 += arr[i][i]
        diag2 += arr[i][len(arr)-1-i]

    return abs(diag1-diag2)

# def diagonalDifference(arr):
#     return abs(sum([row[idx] - row[len(arr)-idx-1] for idx, row in enumerate(arr)]))

# diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]])

def countingSort(arr):
    freq = [0] * 100
    for num in arr:
        freq[num] += 1
    return freq


def pangrams(s):
	# create an array of all letters
	alfa = 'abcdefghijklmnopqrstuvwxyz'
	# check that each letter is in the string
	return 'pangram' if all(l in s.lower() for l in alfa) else 'not pangram'
    # print(result)

# print(pangrams('We promptly judged antique ivory buckles for the next prize'))
# print(pangrams('We promptly judged antique ivory buckles for the prize'))

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    # find the smallest element in B that can meet the condition A + B >= k
    for i in range(len(A)):
        if(A[i] + B[i] < k): return 'NO'
    
    return 'YES'

def birthday(s, d, m):
    c = 0
    # iterate through the s array
    # check each contigeous array of length m
    # if the sum is = d, increment counter
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d: c += 1

    print(c)

birthday([2,2,1,3,2],4,2)