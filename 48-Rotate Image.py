class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
        return matrix

    def anti_rotate(self, matrix):
        for m in matrix:
            m[:] = m[::-1]
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
        return matrix

    def rotate_with_zip(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        return matrix

    def anti_rotate_with_zip(self, matrix):
        for m in matrix:
            m[:] = m[::-1]
        matrix[:] = zip(*matrix)
        return matrix

solution = Solution()
print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.rotate_with_zip([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.anti_rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.anti_rotate_with_zip([[1,2,3],[4,5,6],[7,8,9]]))