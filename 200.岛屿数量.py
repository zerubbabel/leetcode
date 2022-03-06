#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        d=((1,0),(-1,0),(0,1),(0,-1))
        def find(x,y):
            grid[x][y]='0'
            for i in range(4):
                u,v=x+d[i][0],y+d[i][1]
                if 0<=u<m and 0<=v<n and grid[u][v]=='1':
                    find(u,v)

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    find(i,j)
                    ans+=1
        return ans
# @lc code=end

