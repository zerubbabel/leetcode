#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        d=((0,1),(0,-1),(1,0),(-1,0))
        def find(x,y):
            grid[x][y]=1
            for i in range(4):
                u,v=x+d[i][0],y+d[i][1]
                if 0<=u<m and 0<=v<n and grid[u][v]==0:
                    find(u,v)

        for i in range(m):
            if grid[i][0]==0:find(i,0)
            if grid[i][n-1]==0:find(i,n-1)
        for i in range(n):
            if grid[0][i]==0:find(0,i)
            if grid[m-1][i]==0:find(m-1,i)
        ans=0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0:
                    find(i,j)
                    ans+=1
        return ans
# @lc code=end

