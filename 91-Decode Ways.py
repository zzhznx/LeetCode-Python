class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0 or int(s) == 0:
            return 0
        if len(s) == 1 and 0 < int(s) < 10:
            return 1
        if len(s) == 2 and 10 < int(s) <= 26 and int(s[1]) != 0:
            return 2
        dp = [0 for i in range(len(s))]
        dp[0] = 1 if int(s[0]) != 0 else 0

        if dp[0] == 0:
            return 0
        else:
            if int(s[1]) == 0 and int(s[0]) >= 3:
                return 0
            if int(s[1]) == 0 and int(s[0]) <= 2:
                dp[1] = 1
            elif int(s[1]) != 0:
                if int(s[:2]) >= 27:
                    dp[1] = 1
                else:
                    dp[1] = 2

            i = 2
            for c in s[2:]:
                if int(c) == 0 and (int(s[i-1]) == 0 or int(s[i-1]) >= 3):
                    return 0
                elif int(c) == 0 and int(s[i - 1]) != 0:
                    dp[i] = dp[i - 2]
                elif int(s[i-1:i+1]) <= 26 and int(s[i-1]) != 0:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
                i += 1

            #return dp[len(s)-1]
            return dp

solution = Solution()
print(solution.numDecodings("20"))