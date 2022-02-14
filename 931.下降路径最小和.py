#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                t=matrix[i-1][j]
                if j-1>=0:
                    t=min(t,matrix[i-1][j-1])
                if j+1<n:
                    t=min(t,matrix[i-1][j+1])
                matrix[i][j]+=t
        return min(matrix[-1])
# @lc code=end

