# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        # {dummy->1->2->3->4->null}
        current = dummy
        while current.next and current.next.next:
            # current points to dummy in the beginning
            # first -> 1
            first = current.next
            # second -> 2
            second = current.next.next
            # 1 -> 2.next = 3
            first.next = second.next
            # 2 -> 1
            second.next = first
            # now dummy should point to 2
            current.next = second
            # current -> 1
            current = first
            # now { dummy->2->1->3->4 }
        return dummy.next

def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head

head = list_generator([1,2,3,4,5])
solution = Solution()
head = solution.swapPairs(head)
while head:
    print(head.val)
    head = head.next