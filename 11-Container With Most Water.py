class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        MAX = 0
        i = 0
        j = len(height) - 1
        while i != j:
            if height[i] > height[j]:
                area = height[j] * (j - i)
                j -= 1
            else:
                area = height[i] * (j - i)
                i += 1
            if area > MAX:
                MAX = area
        return MAX


solution = Solution()
print(solution.maxArea([1,1,2,2,6,3,2,4,1,5,2]))