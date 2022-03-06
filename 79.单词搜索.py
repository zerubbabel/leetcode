#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
import re


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d=((1,0),(-1,0),(0,1),(0,-1))
        m,n=len(board),len(board[0])
        b=[[0 for i in range(n)] for j in range(m)]
        L=len(word)
        ans=False
        def find(x,y,k):
            if k==L:
                ans=True
                return True
            for i in range(4):
                u,v=x+d[i][0],y+d[i][1]
                if 0<=u<m and 0<=v<n and b[u][v]==0 and board[u][v]==word[k]:
                    b[u][v]=1
                    t=find(u,v,k+1)
                    if t==True:return True
                    b[u][v]=0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    b[i][j]=1
                    t=find(i,j,1)
                    if t==True:return True
                    b[i][j]=0
        return False
# @lc code=end

