class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, low, high):
        if low == high:
            return low
        elif (low + 1) == high:
            if nums[low] > nums[high]:
                return low
            else:
                return high
        else:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
                return self.helper(nums, low, mid - 1)
            else:
                return self.helper(nums, mid + 1, high)

solution = Solution()
print(solution.findPeakElement([1,2,3,4,2,6,7,8,9]))