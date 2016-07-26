class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    def subsets3(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

solution = Solution()
print(solution.subsets([1,2,3]))
print(solution.subsets2([1,2,3]))
print(solution.subsets3([1,2,3]))