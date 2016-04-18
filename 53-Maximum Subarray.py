class Solution(object):
    def maxSubArray(self, nums):
        numsLen = len(nums)
        dp = [0 for i in range(numsLen)]
        dp[0] = nums[0]
        maxSum = dp[0]
        start = 0

        for i in range(1, numsLen):
            dp[i] = max((dp[i-1] + nums[i]), nums[i])
            #maxSum = max(maxSum, dp[i])
        return max(dp)


    #O(1)空间复杂度
    def maxSubArray2(self, nums):
        numsLen = len(nums)
        maxSum = nums[0]
        sum = 0
        for i in range(numsLen):
            sum = max(sum, 0) + nums[i]
            maxSum = max(maxSum, sum)
        return maxSum

solution = Solution()
print(solution.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))