#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from operator import ne


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        d=((1,0),(0,1),(-1,0),(0,-1))
        m,n=len(image),len(image[0])
        oldColor=image[sr][sc]
        if oldColor==newColor:return image
        image[sr][sc]=newColor
        def dfs(x,y,image,m,n):
            for i in range(4):
                u=x+d[i][0]
                v=y+d[i][1]
                if 0<=u<m and 0<=v<n and image[u][v]==oldColor:
                    image[u][v]=newColor
                    dfs(u,v,image,m,n)

        dfs(sr,sc,image,m,n)
        return image
# @lc code=end

