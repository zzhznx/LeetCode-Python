class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for n in nums:
            self.accu += [self.accu[-1] + n]
        print(self.accu)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,2,3,4])
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)