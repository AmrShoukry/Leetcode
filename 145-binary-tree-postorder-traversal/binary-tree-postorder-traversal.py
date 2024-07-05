# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if not root:
            return nodes
        self.postorder(root, nodes)
        return nodes

    def postorder(self, node, nodes):
        if node.left:
            self.postorder(node.left, nodes)
        if node.right:
            self.postorder(node.right, nodes)
        nodes.append(node.val)