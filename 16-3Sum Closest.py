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
        print(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(target - temp) < abs(target - result):
                    if target == temp:
                        return target
                    result = temp
                if temp > target:
                    k -= 1
                else:
                    j += 1
        return result


solution = Solution()
print(solution.threeSumClosest([1,-3,3,5,4,1], 1))
