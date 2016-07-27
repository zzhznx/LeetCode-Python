class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations, reverse=True)
        for i, c in enumerate(citations):
            if c <= (i + 1):
                return i
        return len(citations)

solution = Solution()
print(solution.hIndex([2, 0, 6, 1, 5]))
print(solution.hIndex([100, 99]))
print(solution.hIndex([4, 4, 0, 0]))