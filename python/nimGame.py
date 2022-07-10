# https://www.hackerrank.com/challenges/nim-game-1/problem
# Theory: https://en.wikipedia.org/wiki/Nim

from functools import reduce
def nimGame(pile):
    return 'First' if reduce(lambda x, h: h^x, pile) else 'Second'
