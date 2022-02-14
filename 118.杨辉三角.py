#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows==1:return ans
        for i in range(1,numRows):
            t=[1]
            for j in range(i-1):
                t.append(ans[-1][j]+ans[-1][j+1])
            t.append(1)
            ans.append(t)
        return ans
# @lc code=end

