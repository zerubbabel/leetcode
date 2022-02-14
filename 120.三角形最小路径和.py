#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from numpy import tri


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
# @lc code=end

