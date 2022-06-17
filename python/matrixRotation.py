# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
            
    for i in range(min(m,n)//2):
    # for each ring, convert to one dimentional array
        ring = list(matrix[i][i:n-i])
        ring += [matrix[j][n-1-i] for j in range(i+1,m-1-i)]
        ring += matrix[m-1-i][i:n-i][::-1]
        ring += [matrix[j][i] for j in range(m-2-i,i,-1)] 

        rr = r%len(ring) # ring rotation
        # if rotation is a complete circle, no need to do anything
        if rr == 0:
            continue

        # rotate the ring and construct in reverse order
        # (to use pop() instead of pop(0))
        ring = ring[rr-1::-1] + ring[-1:rr-1:-1]
        # update the matrix
        for j in range(i,n-i):
            matrix[i][j] = ring.pop()
        for j in range(i+1,m-1-i):
            matrix[j][n-i-1] = ring.pop()
        for j in range(n-i-1,i-1,-1):
            matrix[m-i-1][j] = ring.pop()
        for j in range(m-2-i,i,-1):
            matrix[j][i] = ring.pop()
            
    # print the array
    for l in matrix:
        print(*l,sep=' ')
        

# matrixRotation([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],2)

matrixRotation([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],6)
# matrixRotation([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],4)