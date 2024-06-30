# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        stack = []
        length = 0
        current = head
        while current is not None:
            stack.append(current)
            current = current.next
            length += 1
        current = head.next
        head.next = stack.pop()
        tail = head.next
        for i in range((length // 2) - 1):
            tail.next = current
            tail = current
            current = current.next
            tail.next = stack.pop()
            tail = tail.next
        
        if length % 2 != 0:
            tail.next = current
            current.next = None
        else:
            tail.next = None

        