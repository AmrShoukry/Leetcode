# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = self.rec(head)

        if carry == 1:
            node = ListNode(carry, head)
            return node
        return head

    def rec(self, node):
        if node is None:
            return 0
        carry = self.rec(node.next)
        result = node.val * 2 + carry
        value = result % 10
        carry = result // 10
        node.val = value
        return carry