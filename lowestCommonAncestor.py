# return the lowest common ancestor of twe values
def lca(root, v1, v2):
    # if both values are less than the root
    # continue with the left node as new root
    if v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    # if both values are greater than the root
    # continue with the right node as new root
    elif v1> root.info and v2 > root.info:
        return lca(root.right, v1, v2)
    else:
        return root