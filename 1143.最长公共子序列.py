#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        f=[[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    if i>0 and j>0:
                        f[i][j]=f[i-1][j-1]+1
                    else:
                        f[i][j]=1
                else:
                    if i>0 and j>0:
                        f[i][j]=max(f[i-1][j],f[i][j-1],f[i-1][j-1])
                    elif i==0 and j>0:
                        f[i][j]=f[i][j-1]
                    elif j==0 and i>0:
                        f[i][j]=f[i-1][j]
        return f[-1][-1]
# @lc code=end

