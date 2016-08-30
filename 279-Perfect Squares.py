import math

"""
dp[0] = 0
dp[1] = dp[0]+1 = 1
dp[2] = dp[1]+1 = 2
dp[3] = dp[2]+1 = 3
dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 }
      = Min{ dp[3]+1, dp[0]+1 }
      = 1
dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 }
      = Min{ dp[4]+1, dp[1]+1 }
      = 2
.
.
.
dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 }
       = Min{ dp[12]+1, dp[9]+1, dp[4]+1 }
       = 2
.
.
.
dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1
"""


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
