class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrixCols = len(matrix)
        if matrixCols == 0:
            return 0
        matrixRows = len(matrix[0])
        if matrixRows == 0:
            return 0
        longest = 0

        dp = [[0 for i in range(matrixRows)] for j in range(matrixCols)]
        for i in range(matrixCols):
            for j in range(matrixRows):
                dp[i][j] = int(matrix[i][j])
                if int(matrix[i][j]) == 1:
                    longest = 1

        for i in range(1, matrixCols):
            for j in range(1, matrixRows):
                if dp[i][j] == 0:
                    continue
                else:
                    if dp[i-1][j-1] > 0:
                        successStep = 0
                        for step in range(1, dp[i-1][j-1]+1):
                            if dp[i-step][j] > 0 and dp[i][j-step] > 0:
                                successStep += 1
                            else:
                                break
                        dp[i][j] += successStep
                    if dp[i][j] > longest:
                        longest = dp[i][j]
        return longest ** 2


solution = Solution()
print(solution.maximalSquare(["0001","1101","1111","0111","0111"]))
#print(solution.maximalSquare([["0"]]))
