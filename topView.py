# print the nodes that 'visible' from the top

def topView(root):
    top = []
    mx = 0
    mn = 1
    stack = [(root, 0)]
    while stack:
        cur, lvl = stack.pop(0)
        # print(cur, lvl, mn, mx)
        if lvl < mn: 
            top.insert(0, cur.info)
            mn = lvl
        elif lvl > mx:
            top.append(cur.info)
            mx = lvl
        if (cur.left):
            stack.append((cur.left, lvl-1))
        if (cur.right):
            stack.append((cur.right, lvl+1))
    
    print(' '.join(map(str,top)))