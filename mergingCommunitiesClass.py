class Node:
    def __init__(self, data):
        # self.data = data
        self.parent = self
        # self.rank = 0
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
            # if root_a.rank > root_b.rank:
                root_b.parent = root_a
                root_a.size += root_b.size
            # else:
            #     root_a.parent = root_b
            #     root_b.size += root_a.size
            #     if root_a.rank == root_b.rank:
            #         root_b.rank += 1

# n, queries = map(int, input().split())
# for _ in range(Q):

def mergingCommunities(n, queries):
    # Create array of people nodes
    people = [DSF.make_set(i) for i in range(1, n+1)]
    
    # for _ in range(Q):
    # inputs = input().split()
    for q in queries:
        q = q.split(' ')
        if q[0] == 'Q':
            I = int(q[1])
            print(DSF.find(people[I-1]).size)
        elif q[0] == 'M':
            I, J = map(int, q[1:])
            DSF.union(people[I-1], people[J-1])
        
mergingCommunities(3,['Q 1','M 2 1','Q 2', 'M 2 3', 'Q 3', 'Q 2'])