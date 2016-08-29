from collections import Counter
from functools import reduce
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        #return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])
        return reduce(lambda x,y:x+y, [[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

solution = Solution()
print(solution.intersection([1, 2, 2, 2, 1, 3], [2, 2]))