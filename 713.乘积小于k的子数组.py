#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
from operator import le


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        val,left=1,0
        for right in range(n):
            val*=nums[right]
            while val>=k and left<right:
                val//=nums[left]
                left+=1
            if val<k:ans+=right-left+1
        return ans

# @lc code=end

