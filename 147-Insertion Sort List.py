# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        srt = None
        while head:
            node = head
            head = head.next
            node.next = None
            srt = self.insertTo(srt, node)
        return srt

    def insertTo(self, head, node):
        node.next = head
        head = node
        while node.next and node.val > node.next.val:
            node.val, node.next.val = node.next.val, node.val
            node = node.next
        return head

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
head = solution.insertionSortList(node1)
while head:
    print(head.val)
    head = head.next