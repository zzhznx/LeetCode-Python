# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
            if not fast:
                return head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head

head = list_generator([1,2,3,4,5])
solution = Solution()
head = solution.removeNthFromEnd(head, 3)
while head:
    print(head.val)
    head = head.next