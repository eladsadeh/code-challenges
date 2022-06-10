# 3D surface Area Hacker Rank challenge
# return surface area of board described by two dimensional array
# each cooridate A[i][j] describe the height
# calculate the exposed surface area
def surfaceArea(A):
    n = len(A) # number of rows
    m = len(A[0]) # number of columns

    surface = 0
    for r in range(n):
        s = 2*m # bottom and top always exposed
        for c in range(m):
            s += A[r][c] if r-1<0 else max(A[r][c]-A[r-1][c],0)
            s += A[r][c] if r+1>=n else max(A[r][c]-A[r+1][c],0)
            s += A[r][c] if c-1<0 else max(A[r][c]-A[r][c-1],0)
            s += A[r][c] if c+1>=m else max(A[r][c]-A[r][c+1],0)
        
        surface += s

    return surface

print(surfaceArea([[51], [32], [28]]))
    