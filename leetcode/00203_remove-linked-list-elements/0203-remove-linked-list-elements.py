# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        headNode = head

        if headNode == None:
            return None

        while headNode:
            if headNode.val == val:
                headNode = headNode.next
            else:
                break

        # print(headNode)

        node = headNode

        while node != None and node.next and node.next.next:
            if node.next.val == val:
                node.next.val = node.next.next.val
                node.next = node.next.next

            else:
                node = node.next

        if node != None and node.next and node.next.val == val:
            node.next = None

        # print(node)
        # print(headNode)

        return headNode
