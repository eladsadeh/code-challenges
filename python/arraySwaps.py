# https://www.hackerrank.com/challenges/larrys-array/problem
# check if array can be sorted by rotating any 3 consecative
# elements. For general solution, if swaps%(R-1) is 0 -> YES
# R is size of subarray.
def larrysArray(A):
    swaps = 0
    for i in range(len(A)-1):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                swaps += 1
                
    return 'YES' if swaps%2 == 0 else 'NO'