#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        ans=n+1
        i,j=0,0
        for j in range(n):
            sum+=nums[j]
            if sum>=target:
                ans=min(ans,j-i+1)
                while sum>=target and i<j:
                    sum-=nums[i]
                    i+=1
                    if sum>=target:
                        ans=min(ans,j-i+1)
                    
        if ans==n+1:
            return 0
        else:
            return ans
# @lc code=end

