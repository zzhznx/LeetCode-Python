class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pointValueDict = dict()
        for i, n in enumerate(nums):
            if n in pointValueDict:
                return True
            pointValueDict[n] = i

        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,2]))
