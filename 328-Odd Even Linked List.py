# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        evenHead = head.next
        odd = head
        even = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head

node8 = ListNode(8)
node7 = ListNode(7)
node7.next = node8
node6 = ListNode(6)
node6.next = node7
node5 = ListNode(5)
node5.next = node6
node4 = ListNode(4)
node4.next = node5
node3 = ListNode(3)
node3.next = node4
node2 = ListNode(2)
node2.next = node3
node1 = ListNode(1)
node1.next = node2

solution = Solution()
head = solution.oddEvenList(node1)
while head:
    print(head.val)
    head = head.next