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
        for i in range(1, len(nums)):
            if tempNum == nums[i]:
                duplicateCount += 1
            else:
                nums[index] = nums[i]
                index += 1
                tempNum = nums[i]
        nums = nums[:len(nums)-duplicateCount]
        #print(nums)
        return index


solution = Solution()
print(solution.removeDuplicates([1,1,2,3,4,4,5,5]))