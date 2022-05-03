def bfs(n, m, edges, s):
    # Build graph
    graph = {i: set() for i in range(1,n+1)}
    for l, r in edges:
        graph[l].add(r)
        graph[r].add(l)
    
    reached = {}
    # initialize queue with start node and cost = 0
    queue = [(s,0)]
    # set of visited nodes
    seen = {s}
    while queue:
        node, cost = queue.pop(0)
        for nbour in graph[node]:
            if nbour not in seen:
                seen.add(nbour)
                reached[nbour] = cost+6
                queue.append((nbour, cost+6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))
    
    return result