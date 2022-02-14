#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        f=[0]*(n+1)
        f[0],f[1]=1,1
        for i in range(2,n+1):
            for k in range(i):
                f[i]+=f[k]*f[i-1-k]
        return f[-1]

# @lc code=end

