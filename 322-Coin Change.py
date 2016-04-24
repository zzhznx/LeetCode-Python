import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = sys.maxsize
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] >= MAX]

solution = Solution()
print(solution.coinChange([370,417,408,156,143,434,168,83,177,280,117], 9953))
print(solution.coinChange([2], 3))