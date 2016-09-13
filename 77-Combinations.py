class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        resultList = []
        temp = []
        if n < k:
            return resultList
        self.dfs(resultList, temp, k, n, 1)
        return resultList

    def dfs(self, resultList, temp, k, n, m):
        if k == 0:
            result = temp[::]
            resultList.append(result)
            return
        for i in range(m, n-k+2):
            temp.append(i)
            self.dfs(resultList, temp, k-1, n, i + 1)
            temp.pop()

solution = Solution()
print(solution.combine(4, 2))
