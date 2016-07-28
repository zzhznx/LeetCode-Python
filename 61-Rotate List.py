# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy = head
        length = 0
        while dummy:
            length += 1
            dummy = dummy.next

        slow = fast = head
        for i in range(k % length):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        print(slow.val, fast.val)
        fast.next = head
        head = slow.next
        slow.next = None
        return head

def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head


head = list_generator([1, 2, 3, 4, 5, 6])
solution = Solution()
head = solution.rotateRight(head, 2)
while head:
    print(head.val)
    head = head.next