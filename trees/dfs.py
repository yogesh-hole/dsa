class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverseDFS(root: TreeNode):
    if root == None:
        return []
    stack = []
    result = []
    stack.append(root)
    while len(stack):
        current = stack.pop()
        result.append(current.val)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)

    return result


def traverseDFSRecursive(node: TreeNode):
    if node is None:
        return []
    left_values = traverseDFSRecursive(node.left)
    right_values = traverseDFSRecursive(node.right)
    return [node.val, *left_values, *right_values]


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
"""
    a
   /  \
  b    c
 / \    \
d   e    f
   
"""

print(traverseDFS(a))
print(traverseDFSRecursive(a))
