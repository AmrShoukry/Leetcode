# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxValue = [0]
        self.assignDepths(root, maxValue)
        return maxValue[0]

    def assignDepths(self, node, maxValue):
        if not node:
            return 0
        node.depth = 1 + max(self.assignDepths(node.left, maxValue), self.assignDepths(node.right, maxValue))
        acc = 0
        if node.left:
            acc += node.left.depth
        if node.right:
            acc += node.right.depth
        if acc > maxValue[0]:
            maxValue[0] = acc

        return node.depth

