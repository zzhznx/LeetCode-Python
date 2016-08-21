class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j = len(s) - 1
        i = 0
        while i < j:
            while not s[i].isalpha() and i < j:
                i += 1
            while not s[j].isalpha() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

solution = Solution()
print(solution.isPalindrome("0P"))