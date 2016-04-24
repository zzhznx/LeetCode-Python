class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]
        # dpPositive = 1
        # dpNegative = 1
        # maxPro = nums[0]
        #
        # for i in range(0, len(nums)):
        #     dpPositiveTemp = dpPositive
        #     dpPositive = max((dpPositive * nums[i]), (dpNegative * nums[i]), nums[i])
        #     dpNegative = min((dpPositiveTemp * nums[i]), (dpNegative * nums[i]), nums[i])
        #
        #     if dpPositive > maxPro:
        #         maxPro = dpPositive
        # return maxPro
        if len(nums) == 1:
            return nums[0]
        dpPositive = 1
        dpNegative = 1
        maxPro = []

        for i in range(0, len(nums)):
            dpPositiveTemp = dpPositive
            dpPositive = max((dpPositive * nums[i]), (dpNegative * nums[i]), nums[i])
            dpNegative = min((dpPositiveTemp * nums[i]), (dpNegative * nums[i]), nums[i])

            maxPro.append(dpPositive)
        return max(maxPro)

solution = Solution()
print(solution.maxProduct([-4,-3,-2]))
