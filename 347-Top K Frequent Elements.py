class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        bucket = [None] * (len(nums) + 1)
        for n, feq in dic.items():
            if bucket[feq] is None:
                bucket[feq] = []
            bucket[feq].append(n)
        res = []
        pos = len(nums)
        while len(res) < k and pos > 0:
            if bucket[pos] is not None:
                res += bucket[pos]
            pos -= 1
        return res

solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 1))