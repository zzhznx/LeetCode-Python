class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        self.dfs(candidates, n, 0, [], res, k)
        return res

    def dfs(self, nums, target, index, path, res, k):
        if target < 0 or len(path) > k:
            return
        if target == 0:
            if len(path) == k:
                res.append(path)
                return
            else:
                return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res, k)


solution = Solution()
print(solution.combinationSum3(3, 9))
