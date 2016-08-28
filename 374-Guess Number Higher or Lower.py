# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1, n)

    def binarySearch(self, start, end):
        if start > end:
            return -1
        if guess(start) == 0:
            return start
        if guess(end) == 0:
            return end
        mid = (start + end) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            return self.binarySearch(start+1, mid-1)
        else:
            return self.binarySearch(mid+1, end-1)
