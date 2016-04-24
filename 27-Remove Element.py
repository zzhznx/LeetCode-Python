class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # m = 0
        # for n in nums:
        #     if n != val:
        #         nums[m] = n
        #         m += 1
        # print(nums)
        # return m
        nums[:] = filter(lambda x: x != val, nums)
        print(nums)
        return len(nums)

solution = Solution()
print(solution.removeElement([3,2,2,3,3], 3))
