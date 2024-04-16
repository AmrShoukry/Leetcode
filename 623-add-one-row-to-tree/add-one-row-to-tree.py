# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            new_node = TreeNode(val, root)
            return new_node
        
        number_of_max_calls = depth - 2

        self.rec(root, 0, number_of_max_calls, val)

        return root

    def rec(self, root, current_call, number_of_max_calls, value):
        if root is None:
            return
        if current_call == number_of_max_calls:
            new_node_left = TreeNode(value, root.left, None)
            new_node_right = TreeNode(value, None, root.right)
            root.left = new_node_left
            root.right = new_node_right
            return
        self.rec(root.left, current_call + 1, number_of_max_calls, value)
        self.rec(root.right, current_call + 1, number_of_max_calls, value)
            

        