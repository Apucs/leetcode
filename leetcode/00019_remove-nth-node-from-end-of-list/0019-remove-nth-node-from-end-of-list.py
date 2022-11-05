# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        c = 0

        node = head

        while node:
            c += 1
            node = node.next

        target = c-n
        # print(target)

        if target == 0 and head.next == None:
            return None
        elif target == 0:
            return head.next

        count = 0

        start = head

        while count < target-1:
            start = start.next
            count += 1

        start.next = start.next.next

        return head
