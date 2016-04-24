class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point = 0
        for num in nums:
            if num != 0:
                nums[point] = num
                point += 1
        while point < len(nums):
            nums[point] = 0
            point += 1
        print(nums)

solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))
