def arrayManipulation(n, queries):
    arr = [0]*n
    for a,b,k in queries:
        arr[a-1] += k
        if b < n: arr[b] -= k
    
    c = mx = 0
    for e in arr:
        c += e
        if c > mx: mx = c

    return mx
