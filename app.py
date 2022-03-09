'''
 Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
'''

from dis import dis
import enum
from multiprocessing.connection import answer_challenge
from os import wait
import re


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

# birthday([2,2,1,3,2],4,2)


def sumXor(n):
    b = '{0:b}'.format(n)
    c = sum([1 if x == '0' else 0 for x in b])
    return 2 ** c if n > 0 else 1

    # return 1 if n == 0 else 2**(bin(n)[2:].count('0'))

# print(sumXor(0))

def counterGame(n):
    steps = 0
    x = n
    while x > 1:
        print(bin(x)[2:], steps)
        if bin(x)[2:].count('1') == 1:
            x = int(x / 2)
        else:
            x = x - 2**(len(bin(x)[2:])-1)
        
        steps += 1
    print(x, steps)

    print('Louise' if steps % 2 else 'Richard')



# counterGame(1560834904)

def towerBreakers(n, m):
    return 1 if n % 2 else 2

# print(towerBreakers(374625,796723))
def caesarCipher(s, k):

    new_string = ''
    for i in range(len(s)):
        c = s[i]
        if (c.islower()):
            os = 97
        elif (c.isupper()):
            os = 65
        else:
            os = 0

        new_string += chr((ord(c)-os+k)%26+os) if os else c

    return new_string 

# print(caesarCipher('There\'s-a-starman-Waiting', 3))

def superDigit(n, k=1):
    p = n * k
    print(p, len(p))
    if len(p) == 1: return(int(p))

    return superDigit(str(sum([int(d) for d in n])*k))

# print(superDigit('5',4))

def maxMin(k, arr):
    # sort the array
    arr.sort()
    # look for k consecative elements with min diff
    minmax = min([arr[i+k-1]-arr[i] for i in range(len(arr)-k+1)])
    return minmax

# print(maxMin(3,[100,200,300,350,400,401,402]))

def dynamicArray(n, queries):
    # Declare a 2-dimensional array 'arr', of 'n' empty arrays.
    arr = [[] for i in range(n)]
    # Declare an integer, , and initialize it to 0
    lastAnswer = 0
    answers = []

    for query in queries:
        print(f'query {query}')
        idx = (lastAnswer^query[1])%n
        print(idx)
        if query[0] == 1:
            arr[idx].append(query[2])
            print(arr)
        else:
            lastAnswer = arr[idx][query[2]%len(arr[idx])]
            answers.append(lastAnswer)

    return answers

def gridChallenge(grid):
    sorted_grid = [sorted(s) for s in grid ]
    for c in range(len(sorted_grid[0])):
        for r in range(len(grid)-1):
            if sorted_grid[r+1][c] < sorted_grid[r][c]: return 'NO'
    return 'YES'

# print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs','xywuv']))

def balancedSums(arr):
    total = sum(arr)
    suml = 0
  
    for el in arr:
        if suml==total-el-suml: return 'YES'
        suml += el
        

    return 'NO'


# print(balancedSums([5,6,8,10]))

def palindromIndex(s):
    print(s)
    print(s[::-1])
    # if its a palindrom return -1
    if s == s[::-1]: return -1
    for i in range(len(s)):
        s1 = s[:i] + s[i+1:]
        if s1 == s1[::-1]:
            print(s1)
            print(s1[::-1])
            return i

    return -1

# print(palindromIndex('fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf'))

# def getTotalX(a,b):
#     common = []
#     # possible numbers
#     for n in range(max(a), min(b)+1, max(a)):
        
        

# getTotalX([2,4],[16,32,96])
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        displacement = q[i] - i - 1
        if displacement > 2:
            print("Too chaotic")
            return
        else:
            bribes += displacement if displacement > 0 else 0
    
    print(bribes)

# minimumBribes([1,2,5,3,7,8,6,4])

def processLogs(logs, maxSpan):
    users = []
    result = []
    for log in logs:
        id, timespan, activity = log.split(' ')
        
    

processLogs(["99 1 sign-in","100 10 sign-in","50 20 sign-in","100 15 sign-out","50 26 sign-out","99 2 sign-out"],5)