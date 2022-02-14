#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        q=[]
        a=[]
        h,t=0,0
        for i in range(m):
            row=[0]*n
            a.append(row)
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    t+=1
        #BFS put 1 in queue,after search turn 1 into 0
        d=((1,0),(-1,0),(0,1),(0,-1))
        while h<t:
            x,y,step=q[h]
            a[x][y]=step
            h+=1
            for i in range(4):
                u,v=x+d[i][0],y+d[i][1]
                if 0<=u<m and 0<=v<n and mat[u][v]==1:
                    q.append([u,v,step+1])
                    mat[u][v]=0
                    t+=1
        return a
# @lc code=end

