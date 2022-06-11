# permutete array of 1-n so for each i, abs(P[i]-i) == k
# return -1 if its not possible to premutate.
#
def absolutePermutation(n, k):
    if k==0:
    # return the range 1-n
        return [i for i in range(1,n+1)]
    # if n is odd its not possible to permutate, return -1
    elif (n/k)%2 != 0:
        return [-1]
    else:
    # permutete with either i+k or i-k
        return [i+k if ((i-1)//k)%2==0 else i-k for i in range(1,n+1)]
