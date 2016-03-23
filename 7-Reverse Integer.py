class Solution(object):
    def reverse(self, x):
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x = abs(x)
        result = 0
        while x > 0:
            if result * 10 > 2147483647:
                return 0
            result = result * 10 + x % 10
            x //= 10
        result *= sign
        return result

    def reverse2(self, x):
        strX = str(abs(x))
        if x >= 0:
            return 0 if int(strX[::-1]) > 2147483647 else int(strX[::-1])
        else:
            return 0 if int(strX[::-1]) > 2147483647 else int(strX[::-1]) * -1


solution = Solution()
print(solution.reverse2(-123))
