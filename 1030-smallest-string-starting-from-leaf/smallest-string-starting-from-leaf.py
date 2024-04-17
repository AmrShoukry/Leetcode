# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return self.rec(root, None, '')

    def rec(self, root, least, current):
        if root is None:
            return None
        newValue = f'{chr(int(root.val) + 97)}' + current
        if root.left is None and root.right is None:
            if least is None:
                return newValue
            return self.compare(least, newValue)
        return self.compare(self.rec(root.left, least, newValue), self.rec(root.right, least, newValue))

    def compare(self, least1, least2):
        if least1 is None:
            return least2
        if least2 is None:
            return least1
        least1_length = len(least1)
        least2_last_index = len(least2) - 1
        for i in range(least1_length):
            if i > least2_last_index:
                return least2
            if (least2[i] < least1[i]):
                return least2
            elif (least2[i] > least1[i]):
                return least1
        return least1
