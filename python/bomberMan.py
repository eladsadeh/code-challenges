# https://www.hackerrank.com/challenges/bomber-man/problem

def bomberMan(n, grid):
    # return the grid after explosion
    def explodeGrid(grid,x,y):
    # initialize to grid full of bombs
        exploded = [list('O'*x) for _ in range(y)]
    # iterate through the grid
        for r in range(y):
            for c in range(x):
    # if found a bomb in grid, set to '.' for all neighbors
                if grid[r][c] == 'O':
                    exploded[r][c] = '.'
                    exploded[max(0,r-1)][c] = '.'
                    exploded[min(y-1,r+1)][c] = '.'
                    exploded[r][max(c-1,0)] = '.'
                    exploded[r][min(c+1,x-1)] = '.'
        return [''.join(row) for row in exploded]

    # nothing happens for n<2
    if n < 2:
        return grid
    x = len(grid[0])
    y = len(grid)
    # return grid full of bombs for every even second
    if n%2 == 0:
        return ['O' * x] * y
    # return the grid after first explosion for every
    # forth second from 3 on (3,7,11,...)
    first_explosion = explodeGrid(grid,x,y)
    if n%4 == 3:
        return first_explosion
    # return the grid after second explosion for every
    # forth second from 5 on (5,9,13,...)
    return explodeGrid(first_explosion,x,y)

print(bomberMan(3, [
		'.......',
		'...O...',
		'....O..',
		'.......',
		'OO.....',
		'OO.....',
	]))