class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        dp = [[0, 0] for i in range(len(nums))]
        # dp[i][1] means we rob the current house and dp[i][0] means we don't
        for i in range(0, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = nums[i] + dp[i-1][0]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])

    # O(1)空间复杂度
    def rob2(self, nums):
        if len(nums) == 0:
            return 0
        preNo = 0
        preYes = 0
        for i in range(0, len(nums)):
            temp = preYes
            preYes = nums[i] + preNo
            preNo = max(preNo, temp)
        return max(preYes, preNo)

solution = Solution()
print(solution.rob2([4, 4, 3, 5]))