# Minimum cost to build libraries and roads 
# to have all cities connected to a library
# Given possible connection between cities
#
# For n cities that are divided into m groups
# we need m libraries and n - m roads.
# if cost of library < cost of road, than its
# cheaper to build a library in each city.

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road: return c_lib * n

    # find all cities that are in the same cluster
    # the given city. This function traverse through
    # all the cities that are connected to each other.
    def find_cluster(graph, start, visited):
        stack = [start]
        while stack:
    # get the next city in cluster
            city = stack.pop()
            if city not in visited:
    # mark city as visited
                visited.add(city)
    # add connected cities to the stack
                stack.extend(graph[city].difference(visited))

# construct graph as adjacency-list
    graph = {i: set() for i in range(1,n+1)}
    for city1, city2 in cities:
        graph[city1].add(city2)
        graph[city2].add(city1)

# determine number of clusters (CC) in graph
    visited = set() 
    clusters = 0 # number of clusters
    for city in range(1, n+1):
        if city not in visited:
# if city was not visited, it is a new cluster
            clusters += 1
# find all cities in this cluster
            find_cluster(graph, city, visited)

    print(clusters)

    return c_lib * clusters + c_road * (n - clusters)


print(roadsAndLibraries(7, 3, 2, [[1,7],[4,3],[7,6],[1,3],[5,7]]))