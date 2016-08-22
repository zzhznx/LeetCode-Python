class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        result = [0, 1]
        for i in range(1, n):
            result += [(x + 2 ** i) for x in reversed(result)]
        return result

solution = Solution()
print(solution.grayCode(2))