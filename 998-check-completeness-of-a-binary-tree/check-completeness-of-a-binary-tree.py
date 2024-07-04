# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        breadth = [root]
        flag = 0
        while breadth:
            node = breadth.pop(0)
            if not node:
                flag = 1
                continue
            if flag == 1:
                return False
            breadth.append(node.left)
            breadth.append(node.right)
        return True