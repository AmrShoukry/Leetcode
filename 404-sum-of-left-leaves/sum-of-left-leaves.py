# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.getNodeValue(root, 1)

    def getNodeValue(self, node, direction):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            if direction == -1:
                return node.val
            return 0
        return self.getNodeValue(node.left, -1) + self.getNodeValue(node.right, 1)
        