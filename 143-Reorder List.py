# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # find the mid point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        # Reverse the half after middle  1->2->3->4->5->6 to 1->2->3 6->5->4
        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # Merge in-place
        # Start reorder one by one  1->2->3 6->5->4 to 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
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
head = solution.reorderList(head)
while head:
    print(head.val)
    head = head.next