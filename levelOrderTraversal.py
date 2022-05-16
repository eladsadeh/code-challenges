# print the nodes by order for top to bottom
# and left to right (bfs)

def topView(root):
    nodes = []

    stack = [root]
    while stack:
        cur = stack.pop(0)
        nodes.append(cur.info)
        if (cur.left):
            stack.append(cur.left)
        if (cur.right):
            stack.append(cur.right)
    
    print(' '.join(map(str,nodes)))