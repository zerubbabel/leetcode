#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows=rowIndex+1
        ans=[[1]]
        for i in range(1,numRows):
            t=[1]
            for j in range(i-1):
                t.append(ans[-1][j]+ans[-1][j+1])
            t.append(1)
            ans.append(t)
        return ans[rowIndex]
# @lc code=end

