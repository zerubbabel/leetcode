#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        if n<3:return True
        for i in range(2,n):
            if (coordinates[1][0]-coordinates[0][0])*(coordinates[i][1]-coordinates[0][1])!=(coordinates[i][0]-coordinates[0][0])*(coordinates[1][1]-coordinates[0][1]):
                return False
        return True

        

# @lc code=end

