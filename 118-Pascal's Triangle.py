class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # triangle = []
        # triangle.append([1])
        # triangle.append([1,1])
        # if numRows <= 2:
        #     return triangle[:numRows]
        #
        # for row in range(3, numRows+1):
        #     temp = [1]
        #     for col in range(1, row-1):
        #         temp.append(triangle[row-2][col-1] + triangle[row-2][col])
        #     temp.append(1)
        #
        #     triangle.append(temp)
        # return triangle

        '''
        explanation: Any row can be constructed using the offset sum of the previous row. Example:
           1 3 3 1 0
        +  0 1 3 3 1
        =  1 4 6 4 1
        '''

        triangle = [[1]]
        for i in range(1, numRows):
            triangle.append(list(map(lambda x, y: x + y, triangle[-1] + [0], [0] + triangle[-1])))
        return triangle[:numRows]

solution = Solution()
print(solution.generate(5))
