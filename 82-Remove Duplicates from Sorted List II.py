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
            return None
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head.next
        nodeVal = head.val
        while cur is not None:
            if cur.val == nodeVal:
                while cur.val == nodeVal:
                    if cur.next is None:
                        prev.next = None
                        return dummy.next
                    else:
                        cur = cur.next
                prev.next = cur
                nodeVal = cur.val
                cur = cur.next
            else:
                nodeVal = cur.val
                cur = cur.next
                prev = prev.next
        return dummy.next

def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head

head = list_generator([1, 1, 1])
solution = Solution()
head = solution.deleteDuplicates(head)
while head:
    print(head.val)
    head = head.next
