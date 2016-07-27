# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if None in (l1, l2):
            return l1 or l2
        temp = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return temp.next

node5 = ListNode(5)
node4 = ListNode(4)
node4.next = node5
node3 = ListNode(3)
node3.next = node4
node2 = ListNode(2)
node2.next = node3
node1 = ListNode(1)
node1.next = node2

node10 = ListNode(6)
node9 = ListNode(5)
node9.next = node10
node8 = ListNode(2)
node8.next = node9
node7 = ListNode(2)
node7.next = node8
node6 = ListNode(1)
node6.next = node7

solution = Solution()
head = solution.mergeTwoLists(node1, node6)
while head:
    print(head.val)
    head = head.next