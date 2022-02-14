#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b=nums[0],nums[0]#max,min
        ans=nums[0]
        for x in range(1,len(nums)):
            i=nums[x]
            c,d=max(a*i,b*i,i),min(i,a*i,b*i)
            ans=max(ans,c)
            a,b=c,d
        return ans
# @lc code=end

