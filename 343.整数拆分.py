#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        #f=[0]*(n+1)
        f=[0]
        def find(n,k,start,s):
            if n==0:
                if k>=2:
                    f[0]=max(f[0],s)
                return 
            for i in range(start,n+1):
                find(n-i,k+1,i,s*i)
        find(n,0,1,1)
        return f[0]
# @lc code=end

