class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        Don't treat it as a 2D matrix, just treat it as a sorted list
        '''
        if len(matrix) == 0:
            return False
        cols = len(matrix[0])
        l, r = 0, len(matrix[0]) * len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid, matrix[mid // cols][mid % cols])
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


solution = Solution()
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
print(solution.searchMatrix([[1]], 0))