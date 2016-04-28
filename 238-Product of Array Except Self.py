class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        for num in nums:
            output.append(p)
            p *= num

        p = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= p
            p *= nums[i]

        return output

solution = Solution()
print(solution.productExceptSelf([2,3,4,5]))
