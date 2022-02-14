#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        k=-1
        for i in range(len(points)):
            p=points[i]
            if p[0]==x or p[1]==y:
                if k==-1 or abs(x-p[0])+abs(y-p[1])<abs(x-points[k][0])+abs(y-points[k][1]):
                    k=i
                
        return k

# @lc code=end

