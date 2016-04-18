class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            matrix[i][0] = 1
        for j in range(n):
            matrix[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[m-1][n-1]

solution = Solution()
print(solution.uniquePaths(3, 7))