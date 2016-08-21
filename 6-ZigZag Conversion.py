class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        if numRows == 1:
            return s
        size = len(s)
        for i in range(numRows):
            step1 = 2 * (numRows - i - 1)
            step2 = 2 * i
            pos = i
            if pos < size:
                #print("#", pos)
                result += s[pos]
            while True:
                pos += step1
                if pos >= size:
                    break
                if step1:
                    #print("!", pos)
                    result += s[pos]

                pos += step2
                if pos >= size:
                    break
                if step2:
                    #print("@", pos)
                    result += s[pos]
        return result

solution = Solution()
print(solution.convert("PAYPALISHIRING", 4))