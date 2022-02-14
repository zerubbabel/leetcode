#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[]
        for i in range(n):
            dp.append([1]*n)
        ans=1
        for j in range(n):
            for i in range(j-1,-1,-1):
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]=j-i+1
                    else:
                        dp[i][j]=dp[i+1][j-1]+2
                else:
                    if j-i==1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1],dp[i+1][j-1])
                ans=max(ans,dp[i][j])
        return ans

# @lc code=end

