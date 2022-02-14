#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[]
        for i in range(n):
            dp.append([False]*n)
        maxLen=1
        begin=0
        #dp[i][j]=s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
        for j in range(1,n):
            for i in range(0,j):
                dp[i][j]=s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
                if dp[i][j] and j-i+1>maxLen:
                    maxLen=j-i+1
                    begin=i
        return s[begin:begin+maxLen]


# @lc code=end

