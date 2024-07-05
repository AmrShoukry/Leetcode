# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        diff = [999999]
        if not root:
            return 0
        self.inorder(root, nodes, diff)
        return diff[0]

    def inorder(self, node, nodes, diff):
        if node.left:
            self.inorder(node.left, nodes, diff)
        nodes.append(node.val)
        if len(nodes) > 1:
            smallValue = abs(nodes[-1] - nodes[-2])
            if smallValue < diff[0]:
                diff[0] = smallValue
        if node.right:
            self.inorder(node.right, nodes, diff)