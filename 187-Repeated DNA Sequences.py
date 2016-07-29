class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashSet = set()
        repeated = set()
        for i in range(len(s) - 9):
            item = s[i:i+10]
            if item in hashSet:
                repeated.add(item)
            else:
                hashSet.add(item)
        return list(repeated)

solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))