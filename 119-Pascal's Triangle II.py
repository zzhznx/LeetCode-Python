class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex+1):
            row = list(map(lambda x, y: x + y, row + [0], [0] + row))
        return row

solution = Solution()
print(solution.getRow(7))
