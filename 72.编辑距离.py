#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if m==0 and n==0:return 0
        if m==0 and n>0:return n
        if m>0 and n==0:return m 
        f=[[max(m,n) for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if word2[j]==word1[i]:
                    if i>0 and j>0:
                        f[i][j]=min(f[i-1][j-1],f[i-1][j]+1,f[i][j-1]+1)
                    elif i==0 and j>0:
                        f[i][j]=j
                    elif i>0 and j==0:
                        f[i][j]=i
                    else:
                        f[i][j]=0
                else:
                    if i>0 and j>0:
                        f[i][j]=min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
                    elif i==0 and j>0:
                        f[i][j]=f[i][j-1]+1
                    elif i>0 and j==0:
                        f[i][j]=f[i-1][j]+1
                    else:
                        f[i][j]=1
        return f[-1][-1]
# @lc code=end

