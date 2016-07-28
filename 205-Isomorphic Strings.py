class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        done = {}
        for i, j in zip(s, t):
            if i in dic:
                if dic[i] != j:
                    return False
            else:
                if j in done:
                    return False
                dic[i] = j
                done[j] = i
        return True

solution = Solution()
print(solution.isIsomorphic("ab", "aa"))