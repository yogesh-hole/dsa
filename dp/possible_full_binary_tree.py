# public List<TreeNode> allPossibleFBT(int N) {
#                                             //When N is divisible by 2, return an empty list
# List<TreeNode>[] dp = new List[N+1];
# //Base case, when N==1
# dp[1] = new ArrayList<>();
# dp[1].add(new TreeNode(0));
#
# for(int i=3; i<=N; i+=2){
#     dp[i] = new ArrayList<>();
# //Traverse all the possibilities of how to divide the nodes to left and right sides
# for(int j=1; j<i-1; j+=2){
# for(TreeNode l: dp[j]){
# for(TreeNode r: dp[i-j-1]){
#     TreeNode root = new TreeNode(0);
# root.left = l;
# root.right = r;
# dp[i].add(root);
# }
# }
# }
# }
# return dp[N]==null? new ArrayList<>(): dp[N];
# }
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_possible_fbt(n):
    if n % 2 == 0:
        return []
    dp = [[] for _ in range(n + 1)]
    # Base case, when n==1
    dp[1].append(TreeNode(0))
    for i in range(3, n + 1, 2):
        # Traverse all the possibilities of how to divide the nodes to left and right sides
        for j in range(1, i, 2):
            for l in dp[j]:
                for r in dp[i - 1 - j]:
                    dp[i].append(TreeNode(0, left=l, right=r))

        return dp[n]


def allPossibleFBT(N: int) -> List[TreeNode]:
    if N % 2 == 0: return []
    dp = [[] for _ in range(N + 1)]
    dp[1].append(TreeNode(0))
    for n in range(3, N + 1, 2):
        for i in range(1, n, 2):
            j = n - 1 - i
            for left in dp[i]:
                for right in dp[j]:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    dp[n].append(root)
    return dp[N]
# print(all_possible_fbt(5))
print(allPossibleFBT(5))
