class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0]:
            return 0

        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = int((l + r) / 2)
        #     if nums[m] > target:
        #         r = m - 1
        #         if nums[r] < target:
        #             return r + 1
        #     elif nums[m] < target:
        #         l = m + 1
        #         if nums[l] > target:
        #             return l
        #     else:
        #         return m

        low, high, ans = 0, len(nums) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                ans = mid
        return ans

solution = Solution()
print(solution.searchInsert([1, 3, 5], 5))
