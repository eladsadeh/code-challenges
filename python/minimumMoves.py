# this implementation transform the dots on the grid
# to a number that represent the number of moves 
# needed to reach this point, starting from 0
# For example, the followin grid with start = (3,4)
# and end = (0,4) will be modified to
#
# '..X..'    '44X45'
# '....X'    '3323X'
# 'XX.X.' -> 'XX2X1'
# '.....'    '11110'
# '.X..X'    '2X22X'

# and will return '5' as the answer

def minimumMoves(grid, startX, startY, goalX, goalY):
    if startX == goalX and startY == goalY: return 0
    n = len(grid) # grid dimention
    grid = [list(row) for row in grid]
    grid[startX][startY] = 0
    for row in grid: print(row)
    # queue of grid points to explore
    queue = [[startX,startY]]
    # directions: up, down, left, right
    direction =[[-1,0],[1,0],[0,-1],[0,1]]
    # while we have points to explore
    while(len(queue)>0):
    # the current point that is explored
        [row,col] = queue.pop(0)
        moves = grid[row][col] + 1
    # try each direction
        for dr,dc in direction:
            r,c  = row, col
    # while we don't reach the end of the row or 'X'
            while (True):
    # move one step in current direction
                r += dr
                c += dc
                if r<0 or r > n-1 or c<0 or c > n-1 or grid[r][c] == 'X':
                    break
    # if this point was not exlored before
                if grid[r][c] == '.':
    # if its the goal point, return the number of moves
                    if r == goalX and c == goalY:
                        for row in grid: print(row)
                        return moves
    # Otherwise, append to queue and store the number of moves
                    queue.append([r,c])
                    grid[r][c] = moves



print(
	minimumMoves(['..X..', '....X', 'XX.X.', '.....', '.X..X'], 3, 4, 0, 4)
);