import math

class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = self._dp
        while len(dp) <= n:
            dp.append(min(dp[-i*i] for i in range(1, int(math.sqrt(len(dp)) + 1))) + 1)

        return dp[n]

solution = Solution()
print(solution.numSquares(7115))
