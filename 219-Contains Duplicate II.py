class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pointValueDict = dict()
        for i, n in enumerate(nums):
            if n in pointValueDict:
                if i - pointValueDict[n] <= k:
                    return True
            pointValueDict[n] = i

        return False

solution = Solution()
print(solution.containsNearbyDuplicate([1,1], 0))