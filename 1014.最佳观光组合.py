#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        maxi=values[0]+0
        ans=0
        for i in range(1,n):
            ans=max(ans,maxi+values[i]-i)
            maxi=max(maxi,values[i]+i)
        return ans
# @lc code=end

