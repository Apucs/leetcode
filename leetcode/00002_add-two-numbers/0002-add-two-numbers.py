# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = l1
        c1, c2 = 0, 0
        while head:
            c1 += 1
            head = head.next

        head = l2
        while head:
            c2 += 1
            head = head.next

        # print(c1, c2)

        head1, head2 = l1, l2
        # print(head1, head2)

        carry = 0

        if c1 <= c2:
            # print("Less than or equal")
            prev = head1
            while head1:
                val = ((head1.val+head2.val+carry) % 10)
                carry = (head1.val+head2.val+carry)//10
                head1.val = val
                # print(head1)
                prev = head1
                head1 = head1.next
                head2 = head2.next

            head1 = prev
            node = prev = head2

            if c1 != c2:
                while node:
                    val = (node.val + carry) % 10
                    carry = (node.val+carry)//10
                    node.val = val
                    prev = node
                    node = node.next
                print(prev)
                if carry:
                    prev.next = ListNode(carry)
                head1.next = head2
                return l1
            if carry:
                head1.next = ListNode(carry)
            return l1

        else:
            prev = head2
            while head2:
                val = ((head1.val+head2.val+carry) % 10)
                carry = (head1.val+head2.val+carry)//10
                head2.val = val
                # print(head1)

                head1 = head1.next
                prev = head2
                head2 = head2.next

            head2 = prev
            node = prev = head1
            while node:
                val = (node.val+carry) % 10
                carry = (node.val+carry)//10
                node.val = val
                prev = node
                node = node.next
            if carry:
                prev.next = ListNode(carry)
            # print(head2, head1)
            head2.next = head1
            # print(l2)
            return l2
