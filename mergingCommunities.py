def mergingCommunities(n, queries):
    # group dict to store the group of each person
    # {person: group, ...}
    # group = {i: i for i in range(1,n+1)}
    group = list(range(n))
    # size dict to store the size of each group
    # {group: size, ...}
    size = [1]*n
    print(group)
    print(size)
    # for _ in range(q):
    for q in queries:
        q = q.split(' ')
        print(q)
        if q[0] == 'Q':
            print('group:', group[int(q[1])-1])
            print(size[group[int(q[1])-1]])
        elif q[0] == 'M':
            g1,g2 = sorted((group[int(q[1])-1],group[int(q[2])-1]))
            if g1 != g2:
            # move all people in group2 to group1
                for i in range(n):
                    if group[i] == g2:
                        group[i] = g1
                # and adjust the size of the groups
                size[g1] += size[g2]
                size[g2] = 0
                        # size[g1] += 1
                        # size[g2] -=1
            print(group)
            print(size)
        
mergingCommunities(3,['Q 1','M 2 1','Q 2', 'M 2 3', 'Q 3', 'Q 2'])