class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        left = 0
        while left < len(nums)-2 and nums[left] <= 0:
            # 跳过重复的
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
            mid = left + 1
            right = len(nums) - 1
            target = 0 - nums[left]
            while mid < right:
                if (nums[mid] + nums[right]) == target:
                    result.append([nums[left], nums[mid], nums[right]])
                    tempMid = nums[mid]
                    tempRight = nums[right]
                    mid += 1
                    right -= 1
                    while nums[mid] == tempMid and mid < right:
                        mid += 1
                    while nums[right] == tempRight and mid < right:
                        right -= 1
                elif (nums[mid] + nums[right]) > target:
                    right -= 1
                else:
                    mid += 1
            left += 1
        return result

solution = Solution()
print(solution.threeSum([-1,-2,-2,-1,1,1,0,2,2]))
