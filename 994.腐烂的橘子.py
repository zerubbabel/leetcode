#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        days=[]
        for i in range(m):
            t=[1000]*n
            days.append(t)
        d=((1,0),(0,1),(-1,0),(0,-1))
        def dfs(x,y,day):
            for i in range(4):
                u,v=x+d[i][0],y+d[i][1]
                if 0<=u<m and 0<=v<n and grid[u][v]==1 and days[u][v]>day:
                    days[u][v]=day
                    dfs(u,v,day+1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    dfs(i,j,1)
        maxday=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and days[i][j]==1000:
                    return -1
                elif grid[i][j]==1 and days[i][j]!=1000:
                    maxday=max(days[i][j],maxday)
        return maxday
# @lc code=end

