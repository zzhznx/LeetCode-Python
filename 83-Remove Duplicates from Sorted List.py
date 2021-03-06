# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        curr = head.next
        prev = head
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr, curr.next = curr.next, None
            else:
                prev = curr
                curr = curr.next
        return head



node5 = ListNode(3)
node4 = ListNode(3)
node4.next = node5
node3 = ListNode(2)
node3.next = node4
node2 = ListNode(2)
node2.next = node3
node1 = ListNode(1)
node1.next = node2

solution = Solution()
head = solution.deleteDuplicates(node1)
while head:
    print(head.val)
    head = head.next