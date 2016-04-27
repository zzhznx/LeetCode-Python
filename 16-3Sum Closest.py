class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        i = 0
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(target - sum) < abs(target - result):
                    result = sum
                    if target == sum:
                        return target
                if sum > result:
                    k -= 1
                else:
                    j += 1
        return result


solution = Solution()
print(solution.threeSumClosest([-1,-2,-2,-1,1,1,0,2,2], 6))
