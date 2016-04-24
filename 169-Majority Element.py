class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == key:
                count += 1
            else:
                count -= 1
            if count == 0:
                key = nums[i]
                count = 1
        return key


solution = Solution()
print(solution.majorityElement([1,2,3,2,4,2,2]))