class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        nums.reverse()
        # nums = nums[::-1]
        print(nums)

solution = Solution()
solution.rotate([1,2,3,4,5], 3)