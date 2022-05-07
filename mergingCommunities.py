class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0
        self.size = 1

class DSF:
    @staticmethod
    def make_set(data):
        return Node(data)

    @staticmethod
    def find(node):
        # retrun the top level parent
        if node != node.parent:
            node.parent = DSF.find(node.parent)
        return node.parent

    @staticmethod
    def union(node_a, node_b):
        root_a = DSF.find(node_a)
        root_b = DSF.find(node_b)

        if root_a != root_b:
            if root_a.rank > root_b.rank:
                root_b.parent = root_a
                root_a.size += root_b.size
            else:
                root_a.parent = root_b
                root_b.size += root_a.size
                if root_a.rank == root_b.rank:
                    root_b.rank += 1

# N, Q = map(int, input().split())
# # Initialize array of people for 1 - N
# people = [DSF.make_set(i) for i in range(1, N+1)]
# print(people)
# for _ in range(Q):
#     inputs = input().split()
#     if inputs[0] == 'Q':
#         I = int(inputs[1])
#         print(DSF.find(people[I-1]).size)
#     elif inputs[0] == 'M':
#         I, J = map(int, inputs[1:])
        # DSF.union(people[I-1], people[J-1])

def mergingCommunities(n, queries):
    # n, q = map(int, input().split())
    # group dict to store the group of each person
    # {person: group, ...}
    people = [{'parent': i, 'n': i, 'size': 1} for i in range(n)]
    print(people)
    
    def parent_index(n):
        p = people[n]
        while p['parent'] != p['n']:
            p = people[p['parent']-1]
        return p['n']
        
    # for _ in range(Q):
    # inputs = input().split()
    for q in queries:
        q = q.split(' ')
        if q[0] == 'Q':
            I = int(q[1])
            print(parent_index(I-1))
            # print(DSF.find(people[I-1]).size)
        elif q[0] == 'M':
            p1, p2 = parent_index(int(q[1]-1)), parent_index(int(q[2]-1))
   
        
mergingCommunities(3,['Q 1','M 2 1','Q 2', 'M 2 3', 'Q 3', 'Q 2'])