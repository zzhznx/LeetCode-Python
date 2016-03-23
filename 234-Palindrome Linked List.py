class Solution(object):
    '''
    Solution 1: Reversed first half == Second half?
    Phase 1: Reverse the first half while finding the middle.
    Phase 2: Compare the reversed first half with the second half.
    !!!!!如果函数收到的是一个可变对象（比如字典或者列表）的引用,就能修改对象的原始值--相当于通过“传引用”来传递对象。
    如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象--相当于通过“传值'来传递对象
    所以方法一中的head.next变成了None,等于破坏了链表
    '''
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        #长度是奇数
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev

    '''
    Same as the above, but while comparing the two halves,
    restore the list to its original state by reversing the first half back.
    Not that the OJ or anyone else cares.
    方法二就是弥补方法一的不足,把head复原了回去
    '''
    def isPalindrome2(self, head):
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        if fast:
            tail = head.next
        else:
            tail = head
        isPali = True
        while rev:
            isPali = (isPali and rev.val == tail.val)
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPali


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node_1 = ListNode(1)
node_2 = ListNode(2)
node_1.next = node_2
node_3 = ListNode(3)
node_2.next = node_3
node_4 = ListNode(4)
node_3.next = node_4
node_5 = ListNode(5)
node_4.next = node_5

node = node_1
while node:
    print(node.val)
    node = node.next

solution = Solution()
print(solution.isPalindrome2(node_1))

node = node_1
while node:
    print(node.val)
    node = node.next