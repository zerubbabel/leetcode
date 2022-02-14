#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        a=[]
        for i in range(m):
            a.append([0]*n)
        
        a[0][0]=(obstacleGrid[0][0]+1)%2
        for i in range(1,n):
            if obstacleGrid[0][i]==0:
                a[0][i]=a[0][i-1]
        
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                a[i][0]=a[i-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    a[i][j]=a[i-1][j]+a[i][j-1]
        return a[-1][-1]
        
# @lc code=end

