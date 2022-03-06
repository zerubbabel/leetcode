#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
import re


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:return -1
        
        d=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
        n=len(grid)
        if n==1:return 1
        b=[[0 for i in range(n)] for j in range(n)]
        b[0][0]=1
        q=[(0,0,1)]
        head,tail=0,0
        while head<=tail:
            cur=q[head]
            head+=1
            for i in range(8):
                u,v=cur[0]+d[i][0],cur[1]+d[i][1]
                if 0<=u<n and 0<=v<n and b[u][v]==0 and grid[u][v]==0:
                    if u==n-1 and v==n-1:return cur[2]+1
                    q.append((u,v,cur[2]+1))
                    b[u][v]=1
                    tail+=1
        
        return -1
# @lc code=end

