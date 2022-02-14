#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=[[1]*n]#first row
        for i in range(1,m):
            t=[1]+[0]*(n-1)
            a.append(t)
        
        for i in range(1,m):
            for j in range(1,n):
                a[i][j]=a[i-1][j]+a[i][j-1]
        return a[-1][-1]
# @lc code=end

