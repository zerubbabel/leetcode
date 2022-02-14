#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        a,b=0,0#yes,no
        for i in range(n):
            c,d=b+nums[i],max(a,b)
            a,b=c,d
        return max(c,d)

# @lc code=end

