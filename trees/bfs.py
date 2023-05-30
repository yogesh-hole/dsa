class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverseBFS(root):
    if root is None:
        return []
    queue = []
    result = []
    queue.append(root)
    while len(queue):
        current = queue.pop(0)
        result.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return result


# Note: BFS implementation using recursion is not practically feasible.since it needs to maintain 2 stacks,
# it will take O(n^2) complexity.


a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(traverseBFS(a))
