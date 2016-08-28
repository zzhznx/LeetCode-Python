from collections import Counter
import operator
from functools import reduce


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, [ord(x) for x in s + t]))

    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(Counter(t) - Counter(s))[0]