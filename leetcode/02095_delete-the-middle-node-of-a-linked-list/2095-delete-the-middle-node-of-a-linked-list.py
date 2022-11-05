# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = 0

        node = head

        while node:
            n += 1
            node = node.next

        mid = n//2

        if mid == 0:
            head = None
            return head

        count = 0

        start = head

        while count < mid-1:
            start = start.next
            count += 1

        start.next = start.next.next

        return head
