import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j, sum = (0, 0, 0)
        minLen = sys.maxsize
        while j < len(nums):
            sum += nums[j]
            j += 1
            while sum >= s:
                minLen = min(minLen, j-i)
                sum -= nums[i]
                i += 1
        return minLen if minLen < sys.maxsize else 0

solution = Solution()
print(solution.minSubArrayLen(16, [2,3,1,2,4,3]))