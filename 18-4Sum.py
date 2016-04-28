class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        numsLen = len(nums)
        if numsLen < 4:
            return result
        nums.sort()
        for i in range(numsLen-3):
            # 跳过重复的
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[numsLen - 1] + nums[numsLen - 2] + nums[numsLen - 3] < target:
                continue
            for j in range(i+1, numsLen-2):
                if j > (i+1) and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[numsLen - 1] + nums[numsLen - 2] < target:
                    continue
                left = j + 1
                right = numsLen - 1
                while left < right:
                    sumTemp = nums[i] + nums[j] + nums[left] + nums[right]
                    if sumTemp > target:
                        right -= 1
                    elif sumTemp < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        tempLeft = nums[left]
                        tempRight = nums[right]
                        left += 1
                        right -= 1
                        while nums[left] == tempLeft and left < right:
                            left += 1
                        while nums[right] == tempRight and left < right:
                            right -= 1

        return result

solution = Solution()
print(solution.fourSum([0,0,0,0], 0))