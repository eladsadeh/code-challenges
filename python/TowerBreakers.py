# https://www.hackerrank.com/challenges/tower-breakers-1/problem
def towerBreakers(n, m):
    # if n is even, player 2 wins because they can repeat player 1
    # moves. Else player 1 wins. m == 0, player 2 win.
    return 2 if (m == 1 or n%2 == 0) else 1