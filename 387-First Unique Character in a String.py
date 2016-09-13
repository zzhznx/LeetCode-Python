class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for x in s:
            if s.find(x)==s.rfind(x):
                return s.find(x)
        return -1

    def firstUniqChar2(self, s):
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for i, x in enumerate(s):
            if dic[x] == 1:
                return i
        return -1

solution = Solution()
print(solution.firstUniqChar("aaccde"))
print(solution.firstUniqChar2("aaccde"))