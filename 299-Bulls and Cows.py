from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)

solution = Solution()
print(solution.getHint("1807", "7810"))
