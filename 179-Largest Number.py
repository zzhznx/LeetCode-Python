from functools import cmp_to_key

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        nums = sorted(map(str, nums), key=key)
        return ''.join(nums).lstrip('0') or '0'

solution = Solution()
print(solution.largestNumber([13, 9, 5]))
