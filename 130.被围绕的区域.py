#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        if m==1 or n==1:return 
        a=[[board[j][i] for i in range(n)] for j in range(m)]
        t=board
        board=[['X' for i in range(n)] for j in range(m)]
        
        d=((1,0),(-1,0),(0,1),(0,-1))
        def find(x,y,m,n):
            board[x][y]='O'
            for i in range(4):
                u,v=x+d[i][0],y+d[i][1]
                if 0<=u<m and 0<=v<n and a[u][v]=='O' and board[u][v]=='X':
                    find(u,v,m,n)
                
        for i in range(m):
            if a[i][0]=='O':
                find(i,0,m,n)
            if a[i][n-1]=='O':
                find(i,n-1,m,n)
        for i in range(n):
            if a[0][i]=='O':
                find(0,i,m,n)
            if a[m-1][i]=='O':
                find(m-1,i,m,n)
        for i in range(m):
            for j in range(n):
                t[i][j]=board[i][j]
# @lc code=end

