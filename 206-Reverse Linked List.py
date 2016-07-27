# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList2(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)


node5 = ListNode(4)
node4 = ListNode(5)
node4.next = node5
node3 = ListNode(3)
node3.next = node4
node2 = ListNode(6)
node2.next = node3
node1 = ListNode(1)
node1.next = node2

solution = Solution()
head = solution.reverseList(node1)
while head:
    print(head.val)
    head = head.next
head = solution.reverseList2(node5)
while head:
    print(head.val)
    head = head.next
