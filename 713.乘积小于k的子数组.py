#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        val=1
        ans=0
        i,j=0,0
        while j<n:
            while j<n and val*nums[j]<k:
                ans+=1
                val*=nums[j]
                j+=1
            
            val//=nums[i]
            i+=1
        return ans
# @lc code=end

