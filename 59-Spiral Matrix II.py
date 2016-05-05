class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n ** 2):
            matrix[i][j] = k + 1
            if matrix[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj

        return matrix

    def generateMatrix2(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            print("###", list(zip(*A[::-1])))
            A = [[i for i in range(lo, hi)]] + list(zip(*A[::-1]))
            print(A)
        return A


solution = Solution()
print(solution.generateMatrix(4))
print(solution.generateMatrix2(4))