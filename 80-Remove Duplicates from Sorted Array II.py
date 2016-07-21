class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        tempNum = nums[0]
        index = 1
        duplicateCount = 0
        duplicateTime = 1
        for i in range(1, len(nums)):
            if tempNum == nums[i] and duplicateTime == 1:
                nums[index] = nums[i]
                index += 1
                duplicateTime += 1
            elif tempNum == nums[i] and duplicateTime >= 2:
                duplicateCount += 1
            else:
                nums[index] = nums[i]
                index += 1
                tempNum = nums[i]
                duplicateTime = 1
        nums = nums[:len(nums)-duplicateCount]
        #print(nums)
        return index


solution = Solution()
print(solution.removeDuplicates([1,1,2,2,2,3,4,4,5,5]))