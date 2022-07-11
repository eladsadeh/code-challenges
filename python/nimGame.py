# https://www.hackerrank.com/challenges/nim-game-1/problem
# Theory: https://en.wikipedia.org/wiki/Nim

from functools import reduce
def nimGame(pile):
    return 'First' if reduce(lambda x, h: h^x, pile) else 'Second'

# https://www.hackerrank.com/challenges/misere-nim-1/problem
def misereNim(s):
    # all1 = all(map(lambda x: x==1,s))
    # xor = reduce(lambda x,h: x^h, s)
    [xor,all1] = reduce(lambda arr,h: [arr[0]^h, arr[1] and h==1], s, [0,True])
    return 'First' if bool(xor) ^ all1 else 'Second'