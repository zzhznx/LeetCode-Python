class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        r = num
        while r * r > num:
            r = (r + num / r) / 2
        return r * r == num
        """

        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

solution = Solution()
print(solution.isPerfectSquare(16))