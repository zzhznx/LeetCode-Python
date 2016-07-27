class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        low, high = 0, len(citations) - 1
        n = len(citations)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] < n - mid:
                low = mid + 1
            else:
                high = mid - 1
                ans = mid
        return n - ans if ans != -1 else 0

solution = Solution()
print(solution.hIndex([0, 1, 2, 5, 6]))
print(solution.hIndex([99, 100]))
print(solution.hIndex([0, 0, 4, 4]))
print(solution.hIndex([0, 1, 2]))
print(solution.hIndex([0, 0, 0, 0, 0]))