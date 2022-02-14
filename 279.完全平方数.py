#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        coins=[]
        i=1
        while i*i<=n:
            coins.append(i*i)
            i+=1
        m=i-1
        f=[n]*(n+1)
        f[0]=0
        for i in range(m):
            for j in range(coins[i],n+1):
                f[j]=min(f[j],f[j-coins[i]]+1)
        return f[-1]

# @lc code=end

