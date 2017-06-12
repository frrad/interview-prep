import bst


def check_tree(tree, lower_bound=None, upper_bound=None):
    '''return true if tree is BST'''
    if lower_bound and tree.data <= lower_bound:
        return False
    if upper_bound and tree.data >= upper_bound:
        return False

    new_upper = min(upper_bound, tree.data) if upper_bound else tree.data
    if tree.left and not check_tree(tree.left, lower_bound, new_upper):
        return False

    new_lower = max(lower_bound, tree.data) if lower_bound else tree.data
    if tree.right and not check_tree(tree.right, new_lower, upper_bound):
        return False

    return True


tree = bst.bst(19)
tree.insert_list([7, 43, 3, 111, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31])

print tree
print check_tree(tree)
tree.left.data = 20
print tree
print check_tree(tree)
tree.left.data = 7
tree.left.right.data = 20
print tree
print check_tree(tree)
