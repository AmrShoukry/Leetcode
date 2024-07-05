# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root1 = root.left
        root2 = root.right
        return self.checkNode(root1, root2)

    def checkNode(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and not node2:
            return False
        if not node1 and node2:
            return False
        if node1.val != node2.val:
            return False
        return self.checkNode(node1.left, node2.right) and self.checkNode(node1.right, node2.left)
        