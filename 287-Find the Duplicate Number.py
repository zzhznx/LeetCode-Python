class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = int(low + (high - low) / 2)
            print(mid)
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low

solution = Solution()
print(solution.findDuplicate([3, 4, 1, 2, 3]))