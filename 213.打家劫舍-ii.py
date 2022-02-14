#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        #rob 0
        a,b=nums[0],0#yes,no
        c,d=a,b
        for i in range(1,n):
            c,d=nums[i]+b,max(a,b)#yes no
            a,b=c,d
        ans=d
        #not rob 0
        a,b=0,0#yes,no
        c,d=a,b
        for i in range(1,n):
            c,d=b+nums[i],max(a,b)
            a,b=c,d
        return max(ans,max(c,d))

# @lc code=end

