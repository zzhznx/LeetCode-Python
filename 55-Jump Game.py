'''
贪心
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxP = 0
        for i, n in enumerate(nums):
            if i > maxP:
                return False
            maxP = max(maxP, i + n)
            if maxP >= len(nums) - 1:
                return True

solution = Solution()
print(solution.canJump([2, 5, 0, 0]))