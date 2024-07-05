# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxValue = [0]
        self.assignDepths(root)
        self.traverse(root, maxValue)
        return maxValue[0]

    def assignDepths(self, node):
        if not node:
            return 0
        node.depth = 1 + max(self.assignDepths(node.left), self.assignDepths(node.right))
        return node.depth

    def traverse(self, node, maxValue):
        acc = 0
        if not node:
            return
        if node.left:
            acc += node.left.depth
        if node.right:
            acc += node.right.depth
        if acc > maxValue[0]:
            maxValue[0] = acc
        self.traverse(node.left, maxValue)
        self.traverse(node.right, maxValue)
