# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    r = r%((m+n-2)*2)

    # if i-r >=0: x=i-r
    # if i-r >=-m+1: x=0
    # if i-r >=-(m+n-2): x=r-(m-1)-i
    # if i-r >=-(2*m+n-3): x=m-1
    # else: x=r-(m-1)-i