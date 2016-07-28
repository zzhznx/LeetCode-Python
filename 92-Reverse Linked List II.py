# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(m - 1, 0, -1):
            prev = prev.next

        reverse = None
        cur = prev.next
        for i in range(n - m + 1):
            temp = cur.next
            cur.next = reverse
            reverse = cur
            cur = temp
        prev.next.next = cur
        prev.next = reverse

        return dummy.next

def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head

head = list_generator([1, 2, 3, 4, 5, 6])
solution = Solution()
head = solution.reverseBetween(head, 2, 4)
while head:
    print(head.val)
    head = head.next
