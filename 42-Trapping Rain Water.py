class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))