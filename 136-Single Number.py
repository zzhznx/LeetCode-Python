from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

solution = Solution()
print(solution.singleNumber([1,2,3,3,1]))