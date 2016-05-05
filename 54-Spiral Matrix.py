class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0:
            return res
        rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            #Right
            for i in range(colBegin, colEnd + 1):
                print(matrix[rowBegin][i], end=" ")
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            print("Right")

            #Down
            for i in range(rowBegin, rowEnd + 1):
                print(matrix[i][colEnd], end=" ")
                res.append(matrix[i][colEnd])
            colEnd -= 1
            print("Down")

            #Left
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin-1, -1):
                    print(matrix[rowEnd][i], end=" ")
                    res.append(matrix[rowEnd][i])
                rowEnd -= 1
                print("Left")

            #Up
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    print(matrix[i][colBegin], end=" ")
                    res.append(matrix[i][colBegin])
                colBegin += 1
                print("Up")
        return res

    def spiralOrder2(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.spiralOrder([[2, 3]]))
print("solution2")
print(solution.spiralOrder2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(solution.spiralOrder2([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
