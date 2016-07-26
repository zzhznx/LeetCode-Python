class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
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
        return low if nums[low] == target else -1

solution = Solution()
print(solution.search([5,5,1,3], 3))