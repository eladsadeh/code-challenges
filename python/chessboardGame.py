# https://www.hackerrank.com/challenges/a-chessboard-game-1/forum
def chessboardGame(x, y):
    return 'First' if ((x-1)//2)%2 or ((y-1)//2)%2 else 'Second'