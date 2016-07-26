class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        # 求最小的i使得nums[i]等于target，不存在返回-1
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                if nums[mid] == target:
                    ans = mid
        if ans != -1:
            res[0] = ans

            # 求最大的i使得nums[i]等于target，不存在返回-1
            low, high = 0, len(nums) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                    if nums[mid] == target:
                        ans = mid
                else:
                    high = mid - 1
            res[1] = ans
        return res


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 10], 8))
print(solution.searchRange([5, 7, 7, 8, 8, 8, 10], 8))
print(solution.searchRange([5, 7, 7, 8, 8, 8, 10], 3))