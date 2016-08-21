class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        pre = strs[0]
        for i in range(len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[:-1]
        return pre

solution = Solution()
print(solution.longestCommonPrefix(["hello", "hea"]))