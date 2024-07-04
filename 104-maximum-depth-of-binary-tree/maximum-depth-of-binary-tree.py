# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root, 0)

    def getDepth(self, node, counter):
        if node == None:
            return counter
        return max(self.getDepth(node.left, counter + 1), self.getDepth(node.right, counter + 1))