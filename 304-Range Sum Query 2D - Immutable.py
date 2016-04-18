class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.accu = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix))]
        for i, row in enumerate(matrix):
            self.accu[i][1] = row[0]
            for j, data in enumerate(row):
                if j == 0:
                    self.accu[i][j+1] = data
                else:
                    self.accu[i][j+1] = self.accu[i][j] + data
        print(self.accu)


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        for i in range(0, row2 - row1 + 1):
            result += self.sumRange(row1 + i, col1, col2)
        return result

    def sumRange(self, row, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :type row: int
        :rtype: int
        """
        return self.accu[row][j+1] - self.accu[row][i]

# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(numMatrix.sumRegion(0, 0, 0, 0))
# numMatrix.sumRegion(1, 2, 3, 4