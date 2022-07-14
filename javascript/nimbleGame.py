# https://www.hackerrank.com/challenges/nimble-game-1/problem

def nimbleGame(s):
    # count = sum(s[1:])
    # return 'First' if count%2 else 'Second'
    x=0
    for i in range(1,len(s)):
        if s[i]%2:
            x^=i
    return "First" if x else "Second"