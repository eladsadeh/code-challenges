# https://www.hackerrank.com/challenges/nimble-game-1/problem
# Firstly consider, that any even number of coins on the same square can be removed
# If first player wants to maintain the state of the game, he can simply copy second
# player's moves and vice versa  

# Next, we convert this game into a normal "Nim Game", think of the number of spaces 
# that can be removed as the number of objects in a pile.  i.e. a coin on square 3 
# can be moved up to 3 spaces over and you can choose how many spaces 1, 2 or 3 to 
# remove from the "pile"
def nimbleGame(s):
    # count = sum(s[1:])
    # return 'First' if count%2 else 'Second'
    x=0
    for i in range(1,len(s)):
        if s[i]%2:
            x^=i
    return "First" if x else "Second"