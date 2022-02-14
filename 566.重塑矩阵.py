#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        if m*n!=r*c:return mat
        a=[]
        for i in range(r):
            t=[]
            for j in range(c):
                k=i*c+j
                t.append(mat[k//n][k%n])
            a.append(t)
        return a
# @lc code=end

