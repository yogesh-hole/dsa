import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_diff = sys.maxsize

    def find_minimum_differnce(self, root):
        if not root:
            return self.min_diff

        self.find_minimum_differnce(root.left)
        if root.left and root.val - root.left.val:
            self.min_diff = min(self.min_diff, root.val - root.left.val)
        if root.right and root.right.val - root.val:
            self.min_diff = min(self.min_diff, root.right.val - root.val)

        self.find_minimum_differnce(root.right)
        return self.min_diff


if __name__ == '__main__':
    left = Node(-2)
    right = Node(13)
    root = Node(10, left, right)
    s=Solution()
    print(s.find_minimum_differnce(root))
