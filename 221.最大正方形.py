#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
from numpy import mat


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m,n=len(matrix),len(matrix[0])
        dp=[]
        ans=0
        for i in range(m):
            dp.append([0]*n)
        for i in range(n):
            if matrix[0][i]=='1':
                dp[0][i]=1
                ans=1
        for i in range(m):
            if matrix[i][0]=='1':
                dp[i][0]=1
                ans=1
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    ans=max(ans,dp[i][j])
        return ans*ans

# @lc code=end

