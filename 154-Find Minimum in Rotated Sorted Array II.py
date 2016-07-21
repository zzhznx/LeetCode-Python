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
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid
            else:
                start += 1
        return nums[start]

solution = Solution()
print(solution.findMin([7, 8, 9, 0, 1, 2, 3, 4, 5]))
print(solution.findMin([10, 1, 10, 10, 10]))