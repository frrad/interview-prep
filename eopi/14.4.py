import bst


def lca(tree, a, b, lower_bound=float('-inf'), upper_bound=float('inf')):
    if a > b:
        return lca(tree, b, a, lower_bound, upper_bound)

    if tree.left and lower_bound < a < b < tree.data:
        return lca(tree.left, a, b, lower_bound, tree.data)
    if tree.right and tree.data < a < b < upper_bound:
        return lca(tree.right, a, b, tree.data, upper_bound)

    return tree.data


tree = bst.bst(19)
tree.insert_list([7, 43, 3, 111, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31])

print tree
print lca(tree, 31, 17)
