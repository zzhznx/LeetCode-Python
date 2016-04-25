class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i, n in enumerate(digits[::-1]):
            num += n * 10 ** i
        num += 1
        result = []
        while num > 0:
            result.append(num % 10)
            num //= 10
        return result[::-1]

solution = Solution()
print(solution.plusOne([5,11,9]))
