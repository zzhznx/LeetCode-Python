class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointValueDict = dict()
        for i, n in enumerate(nums):
            key = target - n
            if key in pointValueDict:
                result = [pointValueDict[key], i]
                return result
            else:
                pointValueDict[n] = i

solution = Solution()
print(solution.twoSum([2,7,11,15,3], 22))
