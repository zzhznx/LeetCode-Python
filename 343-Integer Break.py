class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return 1
        dp = [1 for i in range(n+1)]
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n+1):
            dp[i] = max(max(j, dp[j]) * max((i-j), dp[i-j]) for j in range(2, i//2+1))

        return dp[n]

solution = Solution()
print(solution.integerBreak(3))
