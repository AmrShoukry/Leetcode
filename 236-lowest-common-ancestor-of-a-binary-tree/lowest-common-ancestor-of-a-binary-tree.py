# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        common = [root]
        found = [0, 0]
        self.traverse(root, common, found, p.val, q.val)
        return common[0]

    def traverse(self, node, common, found, p, q):
        if not node:
            return
        print("C", common[0].val)
        print(node.val)
        if node.val == p:
            found[0] = 1
            print("ppp")
            if found[0] == 1 and found[1] == 1:
                return
            common[0] = node

        if node.val == q:
            found[1] = 1
            print("qqq")
            if found[0] == 1 and found[1] == 1:
                return
            common[0] = node


        if found[0] == 0 and found[1] == 0:
            common[0] = node
        self.traverse(node.left, common, found, p, q)
        if found[0] == 1 and found[1] == 1:
            return
        if node.left == common[0]:
            common[0] = node
        self.traverse(node.right, common, found, p, q)
        if found[0] == 1 and found[1] == 1:
            return
        if node.right == common[0]:
            common[0] = node
