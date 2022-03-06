#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        dx={}#同一竖线上的点数
        for p in points:
            if p[0] not in dx:
                dx[p[0]]=1
            else:
                dx[p[0]]+=1
        ans=max(dx.values())
        def find(i,j):
            if points[i][0]==points[j][0]:return 0
            s=2
            for k in range(j+1,n):
                if (points[j][1]-points[i][1])*(points[k][0]-points[i][0])==(points[k][1]-points[i][1])*(points[j][0]-points[i][0]):
                    s+=1
            return s

        for i in range(n):
            for j in range(i+1,n):
                ans=max(ans,find(i,j))
        return ans
# @lc code=end

