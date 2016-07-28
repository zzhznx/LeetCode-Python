# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = [], []
        while l1 is not None:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2 is not None:
            num2.append(str(l2.val))
            l2 = l2.next
        return self._list_generator(int("".join(reversed(num1))) + int("".join(reversed(num2))))

    def _list_generator(self, num):
        head = prev = ListNode(num % 10)
        num //= 10
        while num:
            node = ListNode(num % 10)
            prev.next = node
            prev = node
            num //= 10
        return head

    def addTwoNumbers2(self, l1, l2):
        dummy = ListNode(-1)
        d = dummy
        d1, d2 = l1, l2
        sum = 0
        while d1 is not None or d2 is not None:
            sum //= 10
            if d1.val is not None:
                sum += d1.val
                d1 = d1.next
            if d2.val is not None:
                sum += d2.val
                d2 = d2.next
            d.next = ListNode(sum % 10)
            d = d.next
        if sum == 10:
            d.next = ListNode(1)
        return dummy.next


def list_generator(nums):
    head = prev = ListNode(nums[0])
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head

list1= list_generator([1, 2, 3])
list2 = list_generator([4, 5, 7])
solution = Solution()
head = solution.addTwoNumbers2(list1, list2)
while head:
    print(head.val)
    head = head.next
