# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node1, node2 = ListNode(-1), ListNode(-1)
        p1, p2 = node1, node2
        while head:
            if head.val < x:
                p1.next = head
                p1 = head
            else:
                p2.next = head
                p2 = head
            head = head.next
        p2.next = None
        p1.next = node2.next
        return node1.next

def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head

head = list_generator([1, 4, 3, 2, 5, 2])
solution = Solution()
head = solution.partition(head, 3)
while head:
    print(head.val)
    head = head.next
