class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        gridCols = len(grid)
        gridRows = len(grid[0])
        '''
        matrix = [[0 for i in range(gridRows)] for j in range(gridCols)]

        matrix[0][0] = grid[0][0]
        for r in range(1, gridRows):
            matrix[0][r] = grid[0][r] + matrix[0][r-1]

        for c in range(1, gridCols):
            matrix[c][0] = grid[c][0] + matrix[c-1][0]

        for c in range(1, gridCols):
            for r in range(1, gridRows):
                matrix[c][r] = min(matrix[c-1][r], matrix[c][r-1]) + grid[c][r]

        return matrix[gridCols-1][gridRows-1]
        '''
        for c in range(0, gridCols):
            for r in range(0, gridRows):
                if c != 0 and r != 0:
                    grid[c][r] = min(grid[c - 1][r], grid[c][r - 1]) + grid[c][r]
                if c == 0 and r != 0:
                    grid[c][r] += grid[c][r-1]
                if c != 0 and r == 0:
                    grid[c][r] += grid[c-1][r]

        return grid[gridCols - 1][gridRows - 1]


solution = Solution()
print(solution.minPathSum([[0,1],[2,6],[3,0]]))