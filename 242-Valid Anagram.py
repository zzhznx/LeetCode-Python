class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram2("anagram", "nagaram"))