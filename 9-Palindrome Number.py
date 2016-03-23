'''
方法非常的巧妙,时间复杂度O(n),空间复杂度O(1),并且比较的是x的一半,不会有sum整数溢出的情况
'''
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        sum = 0
        while x > sum:
            sum = sum * 10 + x % 10
            x //= 10
        return x == sum or sum // 10 == x

solution = Solution()
print(solution.isPalindrome(12321))