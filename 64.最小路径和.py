# @before-stub-for-debug-begin
from python3problem64 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for i in range(1,n):
            grid[0][i]+=grid[0][i-1]
        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if not (i==0 and j==0):
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
# @lc code=end

