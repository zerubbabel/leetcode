#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from numpy import mat


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        i,j=0,m-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid][0]==target:return True
            if matrix[mid][0]>target:
                j=mid-1
            else:
                i=mid+1
        row=j
        i,j=0,n-1
        while i<=j:
            mid=(i+j)//2
            if matrix[row][mid]==target:return True
            if matrix[row][mid]>target:
                j=mid-1
            else:
                i=mid+1
        return False
# @lc code=end

