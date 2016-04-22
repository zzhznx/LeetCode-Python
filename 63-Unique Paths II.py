class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        gridCols = len(obstacleGrid)
        gridRows = len(obstacleGrid[0])
        matrix = [[0 for i in range(gridRows)] for j in range(gridCols)]

        for r in range(gridRows):
            if obstacleGrid[0][r] != 1:
                matrix[0][r] = 1
            else:
                break
        for c in range(gridCols):
            if obstacleGrid[c][0] != 1:
                matrix[c][0] = 1
            else:
                break

        for c in range(1, gridCols):
            for r in range(1, gridRows):
                if obstacleGrid[c][r] == 1:
                    matrix[c][r] = 0
                else:
                    matrix[c][r] = matrix[c-1][r] + matrix[c][r-1]

        return matrix[gridCols-1][gridRows-1]

solution = Solution()
print(solution.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
