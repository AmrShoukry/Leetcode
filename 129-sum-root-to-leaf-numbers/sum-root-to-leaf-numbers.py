# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.rec(root, 0)
    
    def rec(self, root, number):
        if root is None:
            return 0
        new_value = number * 10 + root.val
        if root.left is None and root.right is None:
            return new_value
        return self.rec(root.left, new_value) + self.rec(root.right, new_value)
