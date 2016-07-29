class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashSet = set()
        maxlen = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in hashSet:
                hashSet.add(s[j])
                j += 1
                maxlen = max(maxlen, len(hashSet))
            else:
                hashSet.remove(s[i])
                i += 1
        return maxlen

    def lengthOfLongestSubstring2(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

solution = Solution()
print(solution.lengthOfLongestSubstring2("pwwkew"))