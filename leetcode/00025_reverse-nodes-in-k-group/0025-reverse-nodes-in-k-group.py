# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            # print(kth)
            if not kth:
                break

            groupNext = kth.next

            # Reversing the group

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                # print(groupPrev, dummy)
                tmp = curr.next
                # print("tmp:", tmp)
                # print(groupPrev, dummy)
                curr.next = prev
                # print("curr.next and curr:",curr.next, curr)
                # print(groupPrev, dummy)
                prev = curr
                # print("prev:",prev)
                # print(groupPrev, dummy)
                curr = tmp
                # print(groupPrev, dummy)
                # print("curr:",curr)
                # print()

            # print("Present dummy:", dummy)
            # print("Group previous:", groupPrev, dummy)
            tmp = groupPrev.next
            # print("temp:", tmp, dummy)
            groupPrev.next = kth
            # print("previous next:", groupPrev, dummy)
            groupPrev = tmp
            # print("new previous:",groupPrev, dummy)
            # print()

        # print("\nFinal dummy:", dummy, groupPrev)
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr
