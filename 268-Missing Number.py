class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        sum = numsLen * (numsLen + 1) / 2
        numsSum = 0
        for n in nums:
            numsSum += n
        return int(sum - numsSum)


solution = Solution()
print(solution.missingNumber([0]))