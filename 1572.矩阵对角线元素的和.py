#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        ans=0
        for i in range(n):
            ans+=mat[i][i]
            if i!=n-1-i:
                ans+=mat[i][n-1-i]
        return ans
# @lc code=end

