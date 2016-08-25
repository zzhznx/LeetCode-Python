class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.addPar(res, "", n, 0)
        return res

    def addPar(self, res, str, n, m):
        if n == 0 and m == 0:
            res.append(str)
            return
        if m > 0:
            self.addPar(res, str + ")", n, m - 1)
        if n > 0:
            self.addPar(res, str + "(", n-1, m + 1)

solution = Solution()
print(solution.generateParenthesis(3))