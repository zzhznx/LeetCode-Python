from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for item in strs:
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()

    def groupAnagrams2(self, strs):
        count = Counter([tuple(sorted(x)) for x in strs])
        return filter(lambda x: count[tuple(sorted(x))] > 1, strs)

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
