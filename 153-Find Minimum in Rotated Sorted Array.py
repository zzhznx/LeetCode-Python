class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = int((start + end) / 2)
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        return nums[start]

solution = Solution()
print(solution.findMin([4, 5, 6, 0, 1, 2, 3]))

