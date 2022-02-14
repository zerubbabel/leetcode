#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d=((1,0),(-1,0),(0,1),(0,-1))
        ans=0
        m,n=len(grid),len(grid[0])
        def dfs(x,y):
            grid[x][y]=0
            s=1
            for i in range(4):
                u=x+d[i][0]
                v=y+d[i][1]
                if 0<=u<m and 0<=v<n and grid[u][v]:
                    s+=dfs(u,v)
            return s

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans=max(ans,dfs(i,j))
        return ans
# @lc code=end

