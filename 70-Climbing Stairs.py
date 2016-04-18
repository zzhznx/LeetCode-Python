class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        count = [1 for i in range(n+1)]
        count[2] = 2
        for i in range(3, n+1):
            count[i] = count[i-1] + count[i-2]
        return count[n]

solution = Solution()
print(solution.climbStairs(7))