'''
用罗马数字表示数的基，该方法一般是把若干个罗马数字写成一列，它表示的数等于各个数字所表示的数相加的和。
但是也有例外，当符号 I、X 或 C 位于大数的后面时就作为加数；位于大数的前面就作为减数。
'''
class Solution(object):
    def romanToInt(self, s):
        dictRomanVal = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        i = 0
        while i < len(s) - 1:
            if dictRomanVal[s[i]] < dictRomanVal[s[i+1]]:
                result += (dictRomanVal[s[i+1]] - dictRomanVal[s[i]])
                i += 2
            else:
                result += dictRomanVal[s[i]]
                i += 1
        if i == len(s) - 1:
            result += dictRomanVal[s[i]]
        return result

solution = Solution()
print(solution.romanToInt("IIVI"))