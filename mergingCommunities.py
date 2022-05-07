
def mergingCommunities(n, queries):
    # n, q = map(int, input().split())
    # group dict to store the group of each person
    # {person: group, ...}
    people = [{'parent': i, 'n': i, 'size': 1} for i in range(n)]
    # print(people)
    
    def parent_index(n):
        # p = people[n]
        while people[n]['parent'] != people[n]['n']:
            people[n]['parent'] = people[people[n]['parent']]['parent']
            n = people[n]['parent']
            # print(p)
            # p = people[p['parent']]
        print('lookup:', people)
        return n
        
    # for _ in range(Q):
    # inputs = input().split()
    for q in queries:
        q = q.split(' ')
        if q[0] == 'Q':
            I = int(q[1])
            print('size:', people[parent_index(I-1)]['size'])
            # print(DSF.find(people[I-1]).size)
        elif q[0] == 'M':
            print(q)
            p1, p2 = parent_index(int(q[1])-1), parent_index(int(q[2])-1)
            if p1 != p2:
                people[p2]['parent'] = people[p1]['parent']
                people[p1]['size'] += people[p2]['size']
                print('merge:', people)
        
mergingCommunities(5,['Q 1','M 2 1','Q 2', 'M 2 3','M 4 5', 'Q 3', 'Q 2','M 3 4', 'Q 1', 'Q 5'])