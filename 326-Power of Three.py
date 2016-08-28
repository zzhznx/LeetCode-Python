class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3^19, 3^20 = 3486784401 > maxInt32
        max3PowerInt = 1162261467
        maxInt32 = 2147483647
        if n <= 0 or n > maxInt32:
            return False
        return max3PowerInt % n == 0