class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        for i in range(len(digits)):
            x = int(digits[i])
            if i == 0:
                for c in mapping[x]:
                    ans.append(c)
            while i and len(ans[0]) == i:
                temp = ans.pop(0)
                for c in mapping[x]:
                    ans.append(temp + c)
        return ans

solution = Solution()
print(solution.letterCombinations("23"))
