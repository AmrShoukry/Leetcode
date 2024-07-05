# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        direction = 1
        old = [root]
        new = []
        solution = [[root.val]]
        while new or old:
            while old:
                node = old.pop()
                if direction == 1:
                    if node.right:
                        new.append(node.right)
                    if node.left:
                        new.append(node.left)
                else:
                    if node.left:
                        new.append(node.left)   
                    if node.right:
                        new.append(node.right)
            level = []
            for node in new:                
                level.append(node.val)
            if level:
                solution.append(level)
            old = new
            new = []
            direction *= -1

        return solution