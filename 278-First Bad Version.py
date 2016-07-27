# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        ans = -1
        while low <= high:
            mid = (high + low) // 2
            #if mid < 3:
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid - 1
                ans = mid
        return ans

solution = Solution()
print(solution.firstBadVersion(5))