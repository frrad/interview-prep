import bst


def greater_than(tree, x):
    if not tree:
        return float('inf')

    if tree.data > x:
        return min(tree.data, greater_than(tree.left, x))
    else:
        return greater_than(tree.right, x)


tree = bst.bst(19)
tree.insert_list([7, 43, 3, 111, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31])


print tree
print '\n'.join([str((x, greater_than(tree, x))) for x in xrange(60)])
