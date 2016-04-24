class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        uglyList = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        while len(uglyList) < n:
            newUgly = min(uglyList[p2] * 2, uglyList[p3] * 3, uglyList[p5] * 5)
            uglyList.append(newUgly)
            if newUgly % 2 == 0:
                p2 += 1
            if newUgly % 3 == 0:
                p3 += 1
            if newUgly % 5 == 0:
                p5 += 1
        return uglyList[n-1]

solution = Solution()
print(solution.nthUglyNumber(10))