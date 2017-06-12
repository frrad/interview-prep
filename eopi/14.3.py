import bst


def smallest_k(tree, k):
    ans = []
    if tree.left:
        ans = smallest_k(tree.left, k)
    if len(ans) == k:
        return ans
    ans += [tree.data]
    if len(ans) == k:
        return ans
    if tree.right:
        ans += smallest_k(tree.right, k - len(ans))
    return ans


tree = bst.bst(19)
tree.insert_list([7, 43, 3, 111, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31])

print tree
for i in xrange(20):
    print i,  smallest_k(tree, i)
