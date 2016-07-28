# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast, slow, entry = head, head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None