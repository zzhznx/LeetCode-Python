class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        '''
        bottom up
        空间复杂度O(n)
        '''
        minLen = triangle[len(triangle)-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, len(triangle[i])):
                minLen[j] = triangle[i][j] + min(minLen[j], minLen[j+1])

        return minLen[0]

        '''
        top bottom
        空间复杂度O(n2)
        '''
        # minLen = [[triangle[0][0]]]
        # for j in range(2, len(triangle)+1):
        #     temp = [0 for row in range(j)]
        #     minLen.append(temp)
        #
        # for i in range(1, len(triangle)):
        #     for j in range(0, len(triangle[i])):
        #         if j == 0:
        #             minLen[i][j] = triangle[i][j] + minLen[i-1][j]
        #         elif j == (len(triangle[i])-1):
        #             minLen[i][j] = triangle[i][j] + minLen[i - 1][j-1]
        #         else:
        #             minLen[i][j] = triangle[i][j] + min(minLen[i - 1][j - 1], minLen[i - 1][j])
        #
        # return min(minLen[len(triangle)-1])

solution = Solution()
print(solution.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))