class Solution(object):

    '''
    clockwise rotate
    first reverse up to down, then swap the symmetry
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    '''
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

    '''
    anticlockwise rotate
    first reverse left to right, then swap the symmetry
    1 2 3     3 2 1     3 6 9
    4 5 6  => 6 5 4  => 2 5 8
    7 8 9     9 8 7     1 4 7
    '''
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
print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.rotate_with_zip([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.anti_rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.anti_rotate_with_zip([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
