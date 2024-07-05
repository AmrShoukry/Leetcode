# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.inOrder(root, nodes)
        return nodes[k - 1]

    def inOrder(self, node, nodes):
        if node.left:
            self.inOrder(node.left, nodes)
        nodes.append(node.val)
        if node.right:
            self.inOrder(node.right, nodes)