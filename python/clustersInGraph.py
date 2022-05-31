def componentsInGraph(gb):

# Build graph
    graph = {}
    for l,r in gb:
        if l in graph: 
            graph[l].add(r)
        else: graph[l] = {r}
        if r in graph: 
            graph[r].add(l)
        else: graph[r] = {l}
#   print(graph)
# find all nodes in each cluster and count the number
# of nodes
    visited = set() 
    cluster = 0 # cluster index
    counter = [] # number of nodes in cluster
    for node in graph:
        if node not in visited:
            counter.append(0)
# find all nodes in this cluster start with current node
            stack = [node]
            while stack:
# get the next node in cluster
                n = stack.pop()
                if n not in visited:
                    counter[cluster] += 1
# mark node as visited
                    visited.add(n)
# add connected node to the stack
                    stack.extend(graph[n].difference(visited))
# if node was not visited, it is a new cluster
            cluster += 1
#        print(node, counter)
    return [min(counter), max(counter)]

print(componentsInGraph([[1,5],[1,6],[2,4],[6,7]]))