#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
from numpy import mat, matrix


class NumMatrix:
    matrix=None
    sum=None
    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        m,n=len(self.matrix),len(self.matrix[0])
        
        def getList(m,n):
            a=[]
            for i in range(m):
                t=[0]*n
                a.append(t)
            return a

        self.sum=getList(m,n)
        ans=getList(m,n)

        self.sum[0][0]=self.matrix[0][0]
        for j in range(1,n):
            self.sum[0][j]=self.sum[0][j-1]+self.matrix[0][j]

        for i in range(1,m):
            self.sum[i][0]=self.sum[i-1][0]+self.matrix[i][0]
            for j in range(1,n):
                self.sum[i][j]=self.sum[i-1][j]+self.sum[i][j-1]-self.sum[i-1][j-1]+self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        ans=self.sum[row2][col2]
        if row1>0:
            ans-=self.sum[row1-1][col2]
        if col1>0:
            ans-=self.sum[row2][col1-1]
        if row1>0 and col1>0:
            ans+=self.sum[row1-1][col1-1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.self.sumRegion(row1,col1,row2,col2)
# @lc code=end

