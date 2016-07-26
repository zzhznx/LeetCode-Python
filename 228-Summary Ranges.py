class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges.append([])
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))