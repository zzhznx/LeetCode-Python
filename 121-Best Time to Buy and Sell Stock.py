class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxPro = 0
        for i in range(0, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(prices[i] - minPrice, maxPro)
        return maxPro

solution = Solution()
print(solution.maxProfit([4, 3, 2, 1]))