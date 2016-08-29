class Solution(object):
    def isHappy2(self, n):
        slow = n
        fast = n
        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False

    def isHappy(self, n):
        res = set()
        while not (n in res):
            res.add(n)
            n = self.digitSquareSum(n)
            if n == 1:
                return True
        return False

    def digitSquareSum(self, n):
        sum = 0
        while n > 0:
            tmp = n % 10
            sum += tmp * tmp
            n = n // 10
        return sum


solution = Solution()
print(solution.isHappy(19))
