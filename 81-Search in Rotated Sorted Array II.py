class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return True
            if nums[low] <= nums[mid]:
                if nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return True if nums[low] == target else False

solution = Solution()
print(solution.search([1,3,1,1,1], 3))