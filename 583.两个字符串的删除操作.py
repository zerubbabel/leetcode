#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        f=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,n+1):
            f[0][i]=i
        for i in range(1,m+1):
            f[i][0]=i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    f[i][j]=f[i-1][j-1]
                else:
                    f[i][j]=min(f[i-1][j],f[i][j-1])+1
        return f[m][n]
# @lc code=end

