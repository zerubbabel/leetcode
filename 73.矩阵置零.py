#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        a=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    a.append([i,j])
        for x in a:
            for i in range(n):
                matrix[x[0]][i]=0
            for i in range(m):
                matrix[i][x[1]]=0
        
# @lc code=end

