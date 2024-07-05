# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        flag = [0]
        self.dfs(root, flag, root.val, targetSum)
        return flag[0] == 1

    def dfs(self, node, flag, total, targetSum):
        if not node:
            return
        if flag[0] == 1:
            return
        if total == targetSum and node.left is None and node.right is None:
            flag[0] = 1
        if node.left:
            self.dfs(node.left, flag, total + node.left.val, targetSum)
        if node.right:
            self.dfs(node.right, flag, total + node.right.val, targetSum)