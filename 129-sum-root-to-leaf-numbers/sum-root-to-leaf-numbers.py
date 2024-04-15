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
        arr = []
        result = 0

        self.rec(root, 0, arr)

        for num in arr:
            result += num

        return result
    
    def rec(self, root, number, arr):
        if root.left is None and root.right is None:
            arr.append(number * 10 + root.val)
            return
        if root.left is not None:
            self.rec(root.left, number * 10 + root.val, arr)
        if root.right is not None:
            self.rec(root.right, number * 10 + root.val, arr)
