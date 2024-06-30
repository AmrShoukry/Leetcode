# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        if not current1 and not current2:
            return None
        if not current1:
            head = current2
            return head
        if not current2:
            head = current1
            return head

        if (current1.val <= current2.val):
            head = current1
            current1 = current1.next
        else:
            head = current2
            current2 = current2.next
        current = head

        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        while current1 is not None:
            current.next = current1
            current = current.next
            current1 = current1.next

        while current2 is not None:
            current.next = current2
            current = current.next
            current2 = current2.next

        return head
        