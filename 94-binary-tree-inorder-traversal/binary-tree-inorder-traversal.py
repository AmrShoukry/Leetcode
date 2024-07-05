# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if not root:
            return []
        self.inorder(root, nodes)
        return nodes

    def inorder(self, node, nodes):
        if node.left:
            self.inorder(node.left, nodes)
        nodes.append(node.val)
        if node.right:
            self.inorder(node.right, nodes)