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

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        # print(second)
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # print(prev)

        # print(head)

        first, second = head, prev

        while second:
            # print(first, second)
            tmp1, tmp2 = first.next, second.next
            first.next = second
            first.next.next = tmp1
            # second.next = tmp1
            first, second = tmp1, tmp2
