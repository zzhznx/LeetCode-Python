class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        else:
            num = 0
            mask = 1
            while n >= mask:
                if n & mask:
                    num += 1
                mask <<= 1
            if num == 1:
                return True
            else:
                return False


solution = Solution()
print(solution.isPowerOfTwo(17))
