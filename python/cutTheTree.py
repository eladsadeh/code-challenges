from collections import defaultdict, deque
def cutTheTree(data, edge_data):
    n=len(data)
    tree_sum=sum(data)

#create tree
    tree = {i: set() for i in range(1,n+1)}
    for u,v in edge_data:
        tree[u].add(v)
        tree[v].add(u)
  
# bfs algorithem to save height of each node
    visited=[False]*n
    height=defaultdict(list)
    node_ht={}
# initialize with node 1 (doesn't matter which node we start)
    q=deque([1])
    height[1].append(1)
    node_ht[1]=1
    visited[0]=True
    while q:
        parent=q.popleft()
        h = node_ht[parent]+1
        for child in tree[parent]:
            if visited[child-1] is False:
                node_ht[child]=h
                height[h].append(child)
                visited[child-1]=True
                q.append(child)

# iterating through nodes from bottom to top
# and add value of current node to connected node 
# in the level above
# create dictionary with the total value of each
# node and all its children
    sorted_ht=sorted(height.keys(),reverse=True)
    # node_sum={1:data[0]}
    node_sum={}
# foreach height starting from bottom excluding the top
    for h in sorted_ht[:-1]:
# foreach node in current height
        for node in height[h]:
            node_sum[node]=node_sum.get(node,0)+data[node-1]
            # foreach connected node
            for v in tree[node]:
            # if its a parent node, add the value to the parent
                if v != 1 and node_ht[v]==node_ht[node]-1:
                    node_sum[v]=node_sum.get(v,0)+node_sum[node]
# return the minimum of difference
    return min(abs(tree_sum-node_sum[i]*2) for i in node_sum)