def mergingCommunities(n, queries):
    print(n)
    groups = {i: set([i]) for i in range(1,n+1)}
    size = {i: 1 for i in range(1,n+1)}
    print(size)

    for q in queries:
        

print(mergingCommunities(3,['Q 1','M 1 2','Q 2', 'M 2 3', 'Q 3', 'Q 2']))