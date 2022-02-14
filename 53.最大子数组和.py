#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mm=-10005
        ans,cur=mm,mm
        for x in nums:
            cur=max(cur+x,x)
            ans=max(ans,cur)
        return ans
# @lc code=end

