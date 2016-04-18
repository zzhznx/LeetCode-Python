class Solution(object):
    def rob1(self, nums):
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

    # 重点是破圆
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        # 如果第一个没有被抢
        result1 = self.rob2(nums[1:])
        # 如果第一个被抢
        result2 = self.rob2(nums[2:-1]) + nums[0]
        return max(result1, result2)

solution = Solution()
print(solution.rob([2, 4, 3]))